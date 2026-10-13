#!/usr/bin/env python3
"""List the researchers of the goldener-research RESEARCHERS.md files with their papers.

Usage:
  researchers.py list [--root DIR] [--within TEXT]
      Print every researcher as a JSON list. --within keeps only the researchers
      listed in a file whose path contains TEXT (case-insensitive), e.g. a theme
      directory such as `data_selection`, or `RESEARCHERS.md` for the root file only
      when given exactly as `root`.
  researchers.py find NAME [--root DIR] [--top N]
      Print the researchers whose name best matches NAME as a JSON list, best first,
      each with a `score` (1.0 = same name once normalized; 0.9 when every word
      of NAME is a word of the name, e.g. a surname alone). A score of 0.9 or more
      is a match (several 0.9 matches are ambiguous); lower scores are only candidates to check. NAME `-` reads stdin.
  researchers.py new --base DIR [--root DIR]
      Print the researchers listed under ROOT but not under BASE (by normalized
      name, per file), e.g. ROOT = the tree of a pull request's head commit and
      BASE = the tree of its merge base. Their papers are those listed under ROOT.

Each researcher is {name, affiliation, files, themes, papers}; a researcher listed
in several files is returned once, with the papers of every file merged
(deduplicated by link). Each paper is {title, link, file, note, origin,
first_author, section}; the last four come from the BIBLIOGRAPHY.md entry with the
same link (or, failing that, the same title), and are empty when there is none.
"""
import argparse
import difflib
import html
import json
import re
import sys
from pathlib import Path

ENTRY_RE = re.compile(r"^##\s+👤\s*(?P<name>.+?)\s*$", re.M)
AFFILIATION_RE = re.compile(r"📍\s*Affiliation:\s*(?P<v>.+?)\s*$", re.M)
PAPER_RE = re.compile(r"📄\s*\[(?P<title>.+?)\]\((?P<link>[^)\s]+)\)")
# Bibliography entries, as parsed by skills/paper-review/scripts/papers.py.
BLOCK_RE = re.compile(r"<div>(?P<body>.*?)</div>", re.S)
LINK_TITLE_RE = re.compile(
    r"^\s*<a href=\"(?P<link>[^\"]+)\">\s*<strong>(?P<title>.*?)</strong>\s*</a>", re.S)
AUTHOR_RE = re.compile(r"First author:\s*(?P<v>[^<]*?)\s*</em>")
ORIGIN_RE = re.compile(r"Origin:\s*(?P<v>[^<]*?)\s*</em>")
NOTE_RE = re.compile(r"📝\s*Note:\s*(?P<v>.*?)\s*$", re.S)
HEADING_RE = re.compile(r"^#{2,3}\s+(.*)$", re.M)


def normalize_link(link: str) -> str:
    link = link.strip().rstrip("/")
    return re.sub(r"arxiv\.org/(abs|pdf)/", "arxiv.org/abs/", link).removesuffix(".pdf")


def normalize_text(text: str) -> str:
    return " ".join(re.findall(r"[a-z0-9]+", text.lower()))


def clean_name(heading: str) -> str:
    # Some headings append the affiliation ("Name - University"); keep the name only.
    return heading.split(" - ")[0].strip()


def doc_files(root: Path, name: str):
    files = [root / name] + sorted(
        d / name for d in root.iterdir()
        if d.is_dir() and not d.name.startswith(".") and d.name != "skills")
    return [f for f in files if f.is_file()]


def theme_of(file: str) -> str:
    return "general" if "/" not in file else file.split("/")[0]


def bibliography(root: Path):
    by_link, by_title = {}, {}
    for f in doc_files(root, "BIBLIOGRAPHY.md"):
        text = f.read_text(encoding="utf-8")
        headings = [(m.start(), m.group(1).strip()) for m in HEADING_RE.finditer(text)]
        for block in BLOCK_RE.finditer(text):
            body = block.group("body")
            m = LINK_TITLE_RE.match(body)
            if not m:
                continue
            author, origin = AUTHOR_RE.search(body), ORIGIN_RE.search(body)
            note = NOTE_RE.search(body)
            note = html.unescape(" ".join(note.group("v").split())) if note else ""
            entry = {
                "note": "" if note.lower().startswith("no note provided") else note,
                "origin": html.unescape(origin.group("v")) if origin else "",
                "first_author": html.unescape(author.group("v")) if author else "",
                "section": next((h for pos, h in reversed(headings) if pos < block.start()), ""),
            }
            by_link.setdefault(normalize_link(m.group("link")), entry)
            by_title.setdefault(normalize_text(html.unescape(m.group("title"))), entry)
    return by_link, by_title


def list_researchers(root: Path, within: str = ""):
    by_link, by_title = bibliography(root)
    people = {}
    for f in doc_files(root, "RESEARCHERS.md"):
        file = str(f.relative_to(root))
        if within and not (within.lower() == "root" and file == "RESEARCHERS.md") \
                and within.lower() not in file.lower():
            continue
        text = f.read_text(encoding="utf-8")
        starts = list(ENTRY_RE.finditer(text))
        for i, m in enumerate(starts):
            body = text[m.end(): starts[i + 1].start() if i + 1 < len(starts) else len(text)]
            name = clean_name(html.unescape(m.group("name")))
            person = people.setdefault(normalize_text(name), {
                "name": name, "affiliation": "", "files": [], "themes": [], "papers": []})
            aff = AFFILIATION_RE.search(body)
            if aff and not person["affiliation"]:
                person["affiliation"] = html.unescape(aff.group("v"))
            if file not in person["files"]:
                person["files"].append(file)
                person["themes"].append(theme_of(file))
            seen = {normalize_link(p["link"]) for p in person["papers"]}
            for p in PAPER_RE.finditer(body):
                title, link = html.unescape(p.group("title")).strip(), p.group("link").strip()
                if normalize_link(link) in seen:
                    continue
                seen.add(normalize_link(link))
                bib = by_link.get(normalize_link(link)) or by_title.get(normalize_text(title)) or {
                    "note": "", "origin": "", "first_author": "", "section": ""}
                person["papers"].append({"title": title, "link": link, "file": file, **bib})
    return list(people.values())


def name_score(query: str, name: str) -> float:
    ratio = difflib.SequenceMatcher(None, query, name).ratio()
    # A surname alone, or a name without its middle initial, still matches.
    if set(query.split()) <= set(name.split()):
        ratio = max(ratio, 0.9)
    return round(ratio, 3)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cmd", choices=["list", "find", "new"])
    ap.add_argument("name", nargs="?", help="name to look for (find); - reads it from stdin")
    ap.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[3],
                    help="repository root (default: the repo holding this script)")
    ap.add_argument("--base", type=Path, help="new: the tree to compare ROOT against")
    ap.add_argument("--within", default="", help="list: only researchers of files whose path contains this")
    ap.add_argument("--top", type=int, default=3)
    a = ap.parse_args()

    if a.cmd == "list":
        out = list_researchers(a.root, a.within)
    elif a.cmd == "find":
        if a.name == "-":
            a.name = sys.stdin.read()
        if not a.name or not normalize_text(a.name):
            ap.error("find needs a NAME with at least one letter or digit")
        query = normalize_text(a.name)
        out = sorted(({**p, "score": name_score(query, normalize_text(p["name"]))}
                      for p in list_researchers(a.root)), key=lambda p: -p["score"])[:max(a.top, 1)]
    else:
        if not a.base or not a.base.is_dir():
            ap.error("new needs --base DIR, an existing directory")
        before = {(normalize_text(p["name"]), f) for p in list_researchers(a.base) for f in p["files"]}
        out = [p for p in list_researchers(a.root)
               if any((normalize_text(p["name"]), f) not in before for f in p["files"])]
        for p in out:
            p["new_in"] = [f for f in p["files"] if (normalize_text(p["name"]), f) not in before]
    print(json.dumps(out, indent=1, ensure_ascii=False))


if __name__ == "__main__":
    main()
