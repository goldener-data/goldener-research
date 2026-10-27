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
  OUTREACH_THUNDERBIRD_PROFILE
                           Thunderbird profile directory holding the signature of the
                           OUTREACH_EMAIL account (default: the profiles found in the usual
                           places: ~/.thunderbird, snap, flatpak, macOS); "none" disables
                           the signature

The env file holds one KEY=VALUE per line (`export ` prefix, quotes around the value,
blank lines and `#` comments allowed); only OUTREACH_* keys are read. It should be
readable by its owner only (chmod 600): a warning is printed otherwise.

Usage:
  mailbox.py config
      Print the settings in use (the password is shown only as set / not set), the
      Thunderbird signature found for OUTREACH_EMAIL (or null), and test the login.
  mailbox.py check ADDRESS
      Search every folder, read-only, for messages to, from, cc or bcc ADDRESS, and
      stop with an error if any folder can't be searched. Print {address, total,
      drafts, others, latest: {folder, date, subject}} as JSON: `total` unique
      matching messages (deduplicated by Message-ID across folders), `drafts` those in
      the drafts folder, `others` the rest (a previous exchange); latest is null if
      none. ADDRESS `-` reads the address from stdin.
  mailbox.py draft FILE.eml
      Append FILE.eml to the drafts folder with the \\Draft and \\Seen flags, and
      print {folder, from, signature} as JSON. The From header is set to
      OUTREACH_EMAIL when the file has none. When the Thunderbird account of
      OUTREACH_EMAIL has a signature, it is appended to the plain-text body as
      Thunderbird does (after a "-- " line unless the account suppresses it); an HTML
      signature makes the draft multipart/alternative (plain text + HTML), so it
      opens in Thunderbird's HTML editor with the signature. This script never sends
      anything: it has no SMTP code.
"""
import email
import email.message
import email.policy
import email.utils
import imaplib
import functools
import glob
import html
import html.parser
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


ADDRESS_RE = re.compile(r"[a-z0-9._%+-]+@[a-z0-9-]+(\.[a-z0-9-]+)+")


def check(address):
    if not ADDRESS_RE.fullmatch(address):
        sys.exit(f"not a plain email address (letters, digits, . _ % + - only): {address!r}")
    conn = connect()
    draft_box = drafts_folder(conn)
    # One key per message (Message-ID, else Date + Subject), so that a message seen in several
    # folders (e.g. Gmail's "All Mail" and "Inbox") is counted once.
    seen, in_drafts, latest = set(), set(), None
    q = f'"{address}"'
    for name, flags in folders(conn):
        typ, data = conn.select(name, readonly=True)
        if typ != "OK":
            sys.exit(f"IMAP SELECT {name} failed: {data}; the mailbox could not be fully searched")
        typ, data = conn.uid("SEARCH", None, "OR", "OR", "TO", q, "FROM", q, "OR", "CC", q, "BCC", q)
        if typ != "OK":
            sys.exit(f"IMAP SEARCH in {name} failed: {data}; the mailbox could not be fully searched")
        uids = data[0].split() if data and data[0] else []
        for i in range(0, len(uids), 200):
            typ, msgs = conn.uid("FETCH", b",".join(uids[i:i + 200]).decode(),
                                 "(BODY.PEEK[HEADER.FIELDS (DATE SUBJECT MESSAGE-ID)])")
            if typ != "OK":
                sys.exit(f"IMAP FETCH in {name} failed: {msgs}; the mailbox could not be fully searched")
            for part in msgs:
                if not isinstance(part, tuple):
                    continue
                head = email.message_from_bytes(part[1])
                key = (head["Message-ID"] or "").strip() or f"{head['Date']}|{head['Subject']}"
                seen.add(key)
                if name == draft_box:
                    in_drafts.add(key)
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
    print(json.dumps({"address": address, "total": len(seen), "drafts": len(in_drafts),
                      "others": len(seen - in_drafts), "latest": latest}, ensure_ascii=False))


THUNDERBIRD_PROFILE_GLOBS = (
    "~/.thunderbird/*/prefs.js",
    "~/snap/thunderbird/current/.thunderbird/*/prefs.js",
    "~/snap/thunderbird/current/.config/thunderbird/*/prefs.js",
    "~/.var/app/org.mozilla.Thunderbird/.thunderbird/*/prefs.js",
    "~/Library/Thunderbird/Profiles/*/prefs.js",
)
PREF_RE = re.compile(r'^user_pref\("(?P<key>[^"]+)",\s*(?P<value>"(?:[^"\\]|\\.)*"|true|false|-?\d+)\);', re.M)


def read_prefs(path):
    prefs = {}
    with open(path, encoding="utf-8", errors="replace") as f:
        for m in PREF_RE.finditer(f.read()):
            try:
                prefs[m.group("key")] = json.loads(m.group("value"))
            except ValueError:
                continue
    return prefs


@functools.cache
def signature():
    """{"text", "html" (or None), "separator", "source"} of the OUTREACH_EMAIL account's
    Thunderbird signature, or None when there is none."""
    profile = os.environ.get("OUTREACH_THUNDERBIRD_PROFILE", "")
    if profile.lower() == "none":
        return None
    sender = os.environ.get("OUTREACH_EMAIL", "").lower()
    if profile:
        candidates = [os.path.join(os.path.expanduser(profile), "prefs.js")]
    else:
        candidates = [p for g in THUNDERBIRD_PROFILE_GLOBS for p in glob.glob(os.path.expanduser(g))]
    # The most recently written profile wins when several hold the account.
    for path in sorted(candidates, key=lambda p: os.path.getmtime(p) if os.path.exists(p) else 0,
                       reverse=True):
        if not os.path.isfile(path):
            continue
        prefs = read_prefs(path)
        for key, value in prefs.items():
            m = re.fullmatch(r"mail\.identity\.([^.]+)\.useremail", key)
            if not m or str(value).lower() != sender:
                continue
            ident = f"mail.identity.{m.group(1)}."
            sig_file = prefs.get(ident + "sig_file", "")
            if prefs.get(ident + "attach_signature") and sig_file and os.path.isfile(sig_file):
                with open(sig_file, encoding="utf-8", errors="replace") as f:
                    raw = f.read()
                is_html = sig_file.lower().endswith((".htm", ".html"))
            else:
                raw = prefs.get(ident + "htmlSigText", "")
                is_html = bool(prefs.get(ident + "htmlSigFormat"))
            if not str(raw).strip():
                return None
            if is_html:
                sig_html = re.sub(r"<!--.*?-->", "", raw, flags=re.S).strip()
                sig_text = html_to_text(sig_html)
            else:
                sig_html, sig_text = None, raw.strip("\n")
            return {"text": sig_text, "html": sig_html,
                    "separator": not prefs.get(ident + "suppress_signature_separator"),
                    "source": f"{path} ({m.group(1)}, {'HTML' if is_html else 'plain text'})"}
    return None


class _TextExtractor(html.parser.HTMLParser):
    BLOCKS = {"br", "div", "p", "tr", "table", "li", "h1", "h2", "h3", "h4", "h5", "h6"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts, self.skip = [], 0

    def handle_starttag(self, tag, attrs):
        if tag in ("style", "script", "head"):
            self.skip += 1
        elif tag in self.BLOCKS:
            self.parts.append("\n")
        elif tag == "td":
            self.parts.append(" ")

    def handle_endtag(self, tag):
        if tag in ("style", "script", "head"):
            self.skip = max(0, self.skip - 1)
        elif tag in self.BLOCKS:
            self.parts.append("\n")

    def handle_data(self, data):
        if not self.skip:
            self.parts.append(re.sub(r"\s+", " ", data))


def html_to_text(source):
    parser = _TextExtractor()
    parser.feed(source)
    lines = (re.sub(r"[ \xa0]+", " ", line).strip() for line in "".join(parser.parts).splitlines())
    return "\n".join(line for line in lines if line)


def with_signature(msg, sig):
    """A copy of the text/plain message `msg` with the signature appended to its body."""
    body = msg.get_content().rstrip("\n")
    sep = "-- \n" if sig["separator"] else ""
    out = email.message.EmailMessage(policy=email.policy.SMTP)
    for key, value in msg.items():
        if key.lower() not in ("mime-version", "content-type", "content-transfer-encoding"):
            out[key] = value
    out.set_content(f"{body}\n\n{sep}{sig['text']}\n", cte="8bit")
    if sig["html"]:
        paragraphs = "".join(f"<p>{html.escape(p).replace(chr(10), '<br>')}</p>\n"
                             for p in re.split(r"\n\s*\n", body) if p.strip())
        sep_html = "-- <br>\n" if sig["separator"] else ""
        out.add_alternative(
            "<!DOCTYPE html>\n<html><head><meta http-equiv=\"content-type\" "
            "content=\"text/html; charset=UTF-8\"></head>\n<body>\n"
            f"{paragraphs}<div class=\"moz-signature\">{sep_html}{sig['html']}</div>\n"
            "</body></html>\n", subtype="html", cte="8bit")
    return out


def draft(path):
    with open(path, "rb") as f:
        msg = email.message_from_binary_file(f, policy=email.policy.SMTP)
    if not msg["To"]:
        sys.exit(f"{path} has no To header")
    sender = os.environ.get("OUTREACH_EMAIL", "")
    if not msg["From"]:
        msg["From"] = sender
    sig = signature()
    if sig:
        if msg.get_content_type() != "text/plain" or msg.is_multipart():
            sys.exit(f"{path} is not a plain-text email: can't append the signature "
                     "(set OUTREACH_THUNDERBIRD_PROFILE=none to store it without one)")
        msg = with_signature(msg, sig)
    conn = connect()
    box = drafts_folder(conn)
    typ, data = conn.append(box, "(\\Draft \\Seen)", imaplib.Time2Internaldate(time.time()),
                            msg.as_bytes())
    conn.logout()
    if typ != "OK":
        sys.exit(f"IMAP APPEND to {box} failed: {data}")
    print(json.dumps({"folder": box.strip('"'), "from": str(msg["From"]),
                      "signature": sig["source"] if sig else None}, ensure_ascii=False))


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
                          "drafts_folder": box.strip('"'),
                          "signature": signature()["source"] if signature() else None,
                          "login": "ok"}, ensure_ascii=False))
    elif sys.argv[1] == "check":
        # `-` reads the address from stdin, so it never goes through a shell command line.
        address = sys.stdin.readline() if sys.argv[2] == "-" else sys.argv[2]
        check(address.strip().lower())
    else:
        draft(sys.argv[2])


if __name__ == "__main__":
    main()
