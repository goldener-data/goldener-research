#!/usr/bin/env python3
"""List the papers of the goldener-research bibliography, or find one by title.

Usage:
  papers.py list [--root DIR]
      Print every paper of every BIBLIOGRAPHY.md as a JSON list.
  papers.py find TITLE [--root DIR] [--top N]
      Print the papers whose title best matches TITLE as a JSON list, best
      first, each with a `score` (1.0 = same title once normalized). A score
      of 0.9 or more is a match; lower scores are only candidates to check.
      TITLE `-` reads the title from stdin, so it never goes through the shell.
  papers.py random [--root DIR] [--within TEXT] [--exclude LINK ...]
      Print one paper picked at random as a JSON object. --within keeps only
      the papers whose file or section contains TEXT (case-insensitive), e.g.
      a theme directory or a section heading. --within `-` reads TEXT from stdin.
      --exclude (repeatable) leaves out the paper with that link, e.g. papers
      already drawn whose full text could not be read.

Each paper is {title, link, first_author, origin, file, section}; papers
listed in several files are returned once (deduplicated by link), with the
first matching file and section (--within is applied before deduplication).
"""
import argparse
import difflib
import html
import json
import re
import secrets
import sys
from pathlib import Path

# One entry is one <div>...</div> block; fields are looked up inside the block only, so
# a malformed entry is skipped (or loses a field) without shifting the following ones.
BLOCK_RE = re.compile(r"<div>(?P<body>.*?)</div>", re.S)
LINK_TITLE_RE = re.compile(
    r"^\s*<a href=\"(?P<link>[^\"]+)\">\s*<strong>(?P<title>.*?)</strong>\s*</a>", re.S)
AUTHOR_RE = re.compile(r"First author:\s*(?P<v>[^<]*?)\s*</em>")
ORIGIN_RE = re.compile(r"Origin:\s*(?P<v>[^<]*?)\s*</em>")
HEADING_RE = re.compile(r"^#{2,3}\s+(.*)$", re.M)


def normalize_link(link: str) -> str:
    link = link.strip().rstrip("/")
    return re.sub(r"arxiv\.org/(abs|pdf)/", "arxiv.org/abs/", link).removesuffix(".pdf")


def normalize_title(title: str) -> str:
    return " ".join(re.findall(r"[a-z0-9]+", title.lower()))


def list_papers(root: Path, within: str = ""):
    """Papers of every BIBLIOGRAPHY.md, deduplicated by link. `within` keeps only the
    entries whose file or section contains it, before deduplication, so a paper listed
    under several themes can be found through any of them."""
    needle = within.lower()
    files = [root / "BIBLIOGRAPHY.md"] + sorted(
        d / "BIBLIOGRAPHY.md" for d in root.iterdir()
        if d.is_dir() and not d.name.startswith(".") and d.name != "skills")
    papers, seen = [], set()
    for f in (f for f in files if f.is_file()):
        text = f.read_text(encoding="utf-8")
        headings = [(m.start(), m.group(1).strip()) for m in HEADING_RE.finditer(text)]
        for block in BLOCK_RE.finditer(text):
            body = block.group("body")
            m = LINK_TITLE_RE.match(body)
            if not m:
                continue
            file = str(f.relative_to(root))
            section = next((h for pos, h in reversed(headings) if pos < block.start()), "")
            if needle and needle not in file.lower() and needle not in section.lower():
                continue
            key = normalize_link(m.group("link"))
            if key in seen:
                continue
            seen.add(key)
            author, origin = AUTHOR_RE.search(body), ORIGIN_RE.search(body)
            papers.append({
                "title": html.unescape(" ".join(m.group("title").split())),
                "link": m.group("link").strip(),
                "first_author": html.unescape(author.group("v")) if author else "",
                "origin": html.unescape(origin.group("v")) if origin else "",
                "file": file,
                "section": section,
            })
    return papers


def find(papers, title: str, top: int):
    query = normalize_title(title)
    scored = [{**p, "score": round(difflib.SequenceMatcher(None, query, normalize_title(p["title"])).ratio(), 3)}
              for p in papers]
    return sorted(scored, key=lambda p: -p["score"])[:top]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cmd", choices=["list", "find", "random"])
    ap.add_argument("title", nargs="?", help="title to look for (find); - reads it from stdin")
    ap.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[3],
                    help="repository root (default: the repo holding this script)")
    ap.add_argument("--top", type=int, default=3)
    ap.add_argument("--within", help="random: only papers whose file or section contains this text")
    ap.add_argument("--exclude", action="append", default=[], metavar="LINK",
                    help="random: leave out the paper with this link (repeatable)")
    a = ap.parse_args()
    if a.top < 1:
        ap.error("--top must be 1 or more")

    if a.cmd == "list":
        print(json.dumps(list_papers(a.root), indent=1, ensure_ascii=False))
    elif a.cmd == "random":
        if a.title:
            ap.error("random takes no TITLE; pass a theme or section with --within")
        if a.within == "-":
            a.within = sys.stdin.read().strip()
            if not a.within:
                sys.exit("no theme or section text on stdin for --within -")
        excluded = {normalize_link(link) for link in a.exclude}
        papers = [p for p in list_papers(a.root, a.within or "")
                  if normalize_link(p["link"]) not in excluded]
        if not papers:
            sys.exit("no paper found" + (f" within {a.within!r}" if a.within else "")
                     + (" outside the excluded links" if excluded else ""))
        print(json.dumps(secrets.choice(papers), indent=1, ensure_ascii=False))
    else:
        if a.title == "-":
            a.title = sys.stdin.read()
        if not a.title or not normalize_title(a.title):
            ap.error("find needs a TITLE with at least one letter or digit")
        print(json.dumps(find(list_papers(a.root), a.title, a.top), indent=1, ensure_ascii=False))


if __name__ == "__main__":
    main()
