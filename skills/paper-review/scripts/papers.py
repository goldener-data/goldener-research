#!/usr/bin/env python3
"""List the papers of the goldener-research bibliography, or find one by title.

Usage:
  papers.py list [--root DIR]
      Print every paper of every BIBLIOGRAPHY.md as a JSON list.
  papers.py find TITLE [--root DIR] [--top N]
      Print the papers whose title best matches TITLE as a JSON list, best
      first, each with a `score` (1.0 = same title once normalized). A score
      of 0.9 or more is a match; lower scores are only candidates to check.

Each paper is {title, link, first_author, origin, file, section}; papers
listed in several files are returned once (deduplicated by link).
"""
import argparse
import difflib
import html
import json
import re
from pathlib import Path

ENTRY_RE = re.compile(
    r"<div>\s*<a href=\"(?P<link>[^\"]+)\">\s*<strong>(?P<title>.*?)</strong>\s*</a>"
    r".*?First author:\s*(?P<author>.*?)</em>"
    r".*?Origin:\s*(?P<origin>.*?)</em>",
    re.S,
)
HEADING_RE = re.compile(r"^#{2,3}\s+(.*)$", re.M)


def normalize_link(link: str) -> str:
    link = link.strip().rstrip("/")
    return re.sub(r"arxiv\.org/(abs|pdf)/", "arxiv.org/abs/", link).removesuffix(".pdf")


def normalize_title(title: str) -> str:
    return " ".join(re.findall(r"[a-z0-9]+", title.lower()))


def list_papers(root: Path):
    files = [root / "BIBLIOGRAPHY.md"] + sorted(
        d / "BIBLIOGRAPHY.md" for d in root.iterdir()
        if d.is_dir() and not d.name.startswith(".") and d.name != "skills")
    papers, seen = [], set()
    for f in (f for f in files if f.is_file()):
        text = f.read_text(encoding="utf-8")
        headings = [(m.start(), m.group(1).strip()) for m in HEADING_RE.finditer(text)]
        for m in ENTRY_RE.finditer(text):
            key = normalize_link(m.group("link"))
            if key in seen:
                continue
            seen.add(key)
            papers.append({
                "title": html.unescape(" ".join(m.group("title").split())),
                "link": m.group("link").strip(),
                "first_author": html.unescape(m.group("author").strip()),
                "origin": html.unescape(m.group("origin").strip()),
                "file": str(f.relative_to(root)),
                "section": next((h for pos, h in reversed(headings) if pos < m.start()), ""),
            })
    return papers


def find(papers, title: str, top: int):
    query = normalize_title(title)
    scored = [{**p, "score": round(difflib.SequenceMatcher(None, query, normalize_title(p["title"])).ratio(), 3)}
              for p in papers]
    return sorted(scored, key=lambda p: -p["score"])[:top]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cmd", choices=["list", "find"])
    ap.add_argument("title", nargs="?", help="title to look for (find)")
    ap.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[3],
                    help="repository root (default: the repo holding this script)")
    ap.add_argument("--top", type=int, default=3)
    a = ap.parse_args()

    papers = list_papers(a.root)
    if a.cmd == "list":
        print(json.dumps(papers, indent=1, ensure_ascii=False))
    else:
        if not a.title:
            ap.error("find needs a TITLE")
        print(json.dumps(find(papers, a.title, a.top), indent=1, ensure_ascii=False))


if __name__ == "__main__":
    main()
