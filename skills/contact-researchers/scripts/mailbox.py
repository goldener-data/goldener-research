#!/usr/bin/env python3
"""Check an IMAP mailbox for previous contact with an address, or store a draft in it.

The mailbox is set by environment variables (never by arguments, so the password
never appears in a command line or a log), read from this script's own env file —
OUTREACH_ENV_FILE if set, else ~/.config/goldener-outreach/.env — for any variable
not already set in the environment:
  OUTREACH_IMAP_HOST       IMAP server host name (required)
  OUTREACH_IMAP_PORT       IMAP port (default 993, implicit TLS; 143 uses STARTTLS)
  OUTREACH_EMAIL           login and sender address (required)
  OUTREACH_PASSWORD        password or app password (required, unless
                           OUTREACH_PASSWORD_COMMAND is set)
  OUTREACH_PASSWORD_COMMAND
                           command printing the password on its first output line,
                           run (without a shell) when OUTREACH_PASSWORD is unset,
                           to get it from a vault, e.g.
                             rbw get goldener-outreach            (Bitwarden, via rbw)
                             bw get password goldener-outreach    (Bitwarden CLI)
                             pass show goldener-outreach          (pass)
                             op read op://Private/goldener-outreach/password  (1Password)
                             secret-tool lookup service goldener-outreach   (GNOME keyring)
  OUTREACH_BW_SESSION      Bitwarden CLI session key (from `bw unlock --raw`), given to
                           the password command only, as BW_SESSION
  OUTREACH_DRAFTS_FOLDER   drafts folder (default: the folder flagged \\Drafts,
                           else "Drafts")

The env file holds one KEY=VALUE per line (`export ` prefix, quotes around the value,
blank lines and `#` comments allowed); only OUTREACH_* keys are read. It should be
readable by its owner only (chmod 600): a warning is printed otherwise.

Usage:
  mailbox.py config
      Print the settings in use (the password is shown only as set / not set) and
      test the login.
  mailbox.py check ADDRESS
      Search every folder, read-only, for messages to, from, cc or bcc ADDRESS.
      Print {address, total, drafts, latest: {folder, date, subject}} as JSON
      (`drafts` counts the matches in the drafts folder; latest is null if none).
  mailbox.py draft FILE.eml
      Append FILE.eml to the drafts folder with the \\Draft and \\Seen flags, and
      print {folder, from} as JSON. The From header is set to OUTREACH_EMAIL when
      the file has none. This script never sends anything: it has no SMTP code.
"""
import email
import email.policy
import imaplib
import functools
import json
import os
import re
import shlex
import subprocess
import sys
import time
from email.header import decode_header, make_header

DEFAULT_ENV_FILE = "~/.config/goldener-outreach/.env"
ENV_LINE_RE = re.compile(r"^\s*(?:export\s+)?(?P<key>OUTREACH_[A-Z_]+)\s*=\s*(?P<value>.*?)\s*$")
LIST_RE = re.compile(r'\((?P<flags>[^)]*)\) (?:"[^"]*"|NIL) (?P<name>.+)$')


def load_env_file():
    """Set the OUTREACH_* variables of the env file that aren't already in the environment."""
    path = os.path.expanduser(os.environ.get("OUTREACH_ENV_FILE") or DEFAULT_ENV_FILE)
    if not os.path.isfile(path):
        if os.environ.get("OUTREACH_ENV_FILE"):
            sys.exit(f"OUTREACH_ENV_FILE points to a missing file: {path}")
        return None
    if os.stat(path).st_mode & 0o077:
        print(f"warning: {path} is readable by other users; run chmod 600 on it", file=sys.stderr)
    with open(path, encoding="utf-8") as f:
        for line in f:
            if not line.strip() or line.lstrip().startswith("#"):
                continue
            m = ENV_LINE_RE.match(line)
            if not m:
                continue
            value = m.group("value")
            if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
                value = value[1:-1]
            os.environ.setdefault(m.group("key"), value)
    return path


@functools.cache
def password():
    """OUTREACH_PASSWORD, else the first output line of OUTREACH_PASSWORD_COMMAND."""
    if os.environ.get("OUTREACH_PASSWORD"):
        return os.environ["OUTREACH_PASSWORD"], "variable"
    command = os.environ.get("OUTREACH_PASSWORD_COMMAND", "")
    if not command:
        return "", ""
    env = dict(os.environ)
    if env.get("OUTREACH_BW_SESSION"):
        env["BW_SESSION"] = env["OUTREACH_BW_SESSION"]
    try:
        out = subprocess.run(shlex.split(command), capture_output=True, text=True,
                             stdin=subprocess.DEVNULL, env=env, timeout=60)
    except (OSError, ValueError, subprocess.TimeoutExpired) as e:
        sys.exit(f"OUTREACH_PASSWORD_COMMAND failed to run: {type(e).__name__}: {e}")
    # Never show the command's output: only its exit status and error stream.
    if out.returncode != 0:
        sys.exit(f"OUTREACH_PASSWORD_COMMAND exited with {out.returncode}: "
                 + (out.stderr.strip().splitlines() or [""])[-1][:300]
                 + " (is the vault unlocked? `bw` needs OUTREACH_BW_SESSION or BW_SESSION)")
    pwd = (out.stdout.splitlines() or [""])[0].strip()
    if not pwd:
        sys.exit("OUTREACH_PASSWORD_COMMAND printed no password (is the vault unlocked? "
                 "`bw` needs OUTREACH_BW_SESSION or BW_SESSION; check the item name)")
    return pwd, "command"


def settings():
    host, user = (os.environ.get(k, "") for k in ("OUTREACH_IMAP_HOST", "OUTREACH_EMAIL"))
    missing = [k for k, v in (("OUTREACH_IMAP_HOST", host), ("OUTREACH_EMAIL", user)) if not v]
    pwd = ""
    if not missing:
        pwd, _ = password()
        if not pwd:
            missing.append("OUTREACH_PASSWORD or OUTREACH_PASSWORD_COMMAND")
    if missing:
        where = os.path.expanduser(os.environ.get("OUTREACH_ENV_FILE") or DEFAULT_ENV_FILE)
        sys.exit("missing variable(s): " + ", ".join(missing)
                 + f" (set them in {where} or in the environment)")
    port = int(os.environ.get("OUTREACH_IMAP_PORT") or 993)
    return host, port, user, pwd


def connect():
    host, port, user, pwd = settings()
    try:
        if port == 143:
            conn = imaplib.IMAP4(host, port)
            conn.starttls()
        else:
            conn = imaplib.IMAP4_SSL(host, port)
        conn.login(user, pwd)
    except (imaplib.IMAP4.error, OSError) as e:
        sys.exit(f"IMAP connection to {host}:{port} as {user} failed: {e}")
    return conn


def folders(conn):
    """[(name, flags)] of the selectable folders, names quoted for IMAP commands."""
    typ, data = conn.list()
    if typ != "OK":
        sys.exit("IMAP LIST failed")
    out = []
    for line in data:
        m = LIST_RE.match(line.decode("utf-8", "replace") if isinstance(line, bytes) else str(line))
        if not m or "\\Noselect" in m.group("flags") or "\\NonExistent" in m.group("flags"):
            continue
        name = m.group("name").strip()
        if not name.startswith('"'):
            name = '"' + name.replace("\\", "\\\\").replace('"', '\\"') + '"'
        out.append((name, m.group("flags")))
    return out


def drafts_folder(conn):
    wanted = os.environ.get("OUTREACH_DRAFTS_FOLDER")
    if wanted:
        return '"' + wanted.replace("\\", "\\\\").replace('"', '\\"') + '"'
    found = next((n for n, f in folders(conn) if "\\Drafts" in f), None)
    return found or '"Drafts"'


def decoded(value):
    return str(make_header(decode_header(value))) if value else ""


def check(address):
    if not re.fullmatch(r"[^@\s\"()]+@[^@\s\"()]+\.[^@\s\"()]+", address):
        sys.exit(f"not an email address: {address!r}")
    conn = connect()
    draft_box = drafts_folder(conn)
    total, drafts, latest = 0, 0, None
    for name, flags in folders(conn):
        # On Gmail, "All Mail" repeats every other folder: skip it to avoid double counts,
        # except for spam and trash, which it doesn't hold and which are still searched.
        if "\\All" in flags:
            continue
        typ, _ = conn.select(name, readonly=True)
        if typ != "OK":
            continue
        q = f'"{address}"'
        typ, data = conn.uid("SEARCH", None, "OR", "OR", "TO", q, "FROM", q, "OR", "CC", q, "BCC", q)
        uids = data[0].split() if typ == "OK" and data and data[0] else []
        total += len(uids)
        if name == draft_box:
            drafts += len(uids)
        for uid in uids[-5:]:
            typ, msg = conn.uid("FETCH", uid, "(BODY.PEEK[HEADER.FIELDS (DATE SUBJECT)])")
            if typ != "OK" or not msg or not isinstance(msg[0], tuple):
                continue
            head = email.message_from_bytes(msg[0][1])
            try:
                when = email.utils.parsedate_to_datetime(head["Date"]).timestamp()
            except (TypeError, ValueError):
                when = 0
            if latest is None or when > latest["_ts"]:
                latest = {"folder": name.strip('"'), "date": head["Date"] or "",
                          "subject": decoded(head["Subject"]), "_ts": when}
    conn.logout()
    if latest:
        latest.pop("_ts")
    print(json.dumps({"address": address, "total": total, "drafts": drafts, "latest": latest},
                     ensure_ascii=False))


def draft(path):
    with open(path, "rb") as f:
        msg = email.message_from_binary_file(f, policy=email.policy.SMTP)
    if not msg["To"]:
        sys.exit(f"{path} has no To header")
    sender = os.environ.get("OUTREACH_EMAIL", "")
    if not msg["From"]:
        msg["From"] = sender
    conn = connect()
    box = drafts_folder(conn)
    typ, data = conn.append(box, "(\\Draft \\Seen)", imaplib.Time2Internaldate(time.time()),
                            msg.as_bytes())
    conn.logout()
    if typ != "OK":
        sys.exit(f"IMAP APPEND to {box} failed: {data}")
    print(json.dumps({"folder": box.strip('"'), "from": str(msg["From"])}, ensure_ascii=False))


def main():
    env_file = load_env_file()
    if len(sys.argv) < 2 or sys.argv[1] not in ("config", "check", "draft") \
            or (sys.argv[1] != "config" and len(sys.argv) != 3):
        sys.exit(__doc__)
    if sys.argv[1] == "config":
        host, port, user, _ = settings()
        conn = connect()
        box = drafts_folder(conn)
        conn.logout()
        print(json.dumps({"env_file": env_file, "host": host, "port": port, "email": user,
                          "password": "from OUTREACH_PASSWORD" if password()[1] == "variable"
                          else "from OUTREACH_PASSWORD_COMMAND",
                          "drafts_folder": box.strip('"'), "login": "ok"}))
    elif sys.argv[1] == "check":
        check(sys.argv[2].strip().lower())
    else:
        draft(sys.argv[2])


if __name__ == "__main__":
    main()
