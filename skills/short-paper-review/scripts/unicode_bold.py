#!/usr/bin/env python3
"""Turn **marked** spans of a text into Unicode bold, for targets that don't render Markdown.

Usage:
  unicode_bold.py [FILE]
      Read FILE (or stdin when FILE is missing or `-`) and print it with every
      **span** replaced by Mathematical Sans-Serif Bold characters (LinkedIn, X,
      Bluesky, Threads show them as bold). Only ASCII letters and digits change;
      other characters (spaces, accents, punctuation, emoji) are kept as they are.
      URLs, @handles and #hashtags inside a span are left unchanged, so they stay
      clickable. Unmatched `**` are left as they are.
"""
import re
import sys

URL_OR_TAG_RE = re.compile(r"(https?://\S+|[@#]\w+)")


def bold_char(c: str) -> str:
    if "A" <= c <= "Z":
        return chr(0x1D5D4 + ord(c) - ord("A"))
    if "a" <= c <= "z":
        return chr(0x1D5EE + ord(c) - ord("a"))
    if "0" <= c <= "9":
        return chr(0x1D7EC + ord(c) - ord("0"))
    return c


def bold(text: str) -> str:
    # Odd parts of the split are URLs, handles or hashtags: keep them as typed.
    return "".join(p if i % 2 else "".join(map(bold_char, p))
                   for i, p in enumerate(URL_OR_TAG_RE.split(text)))


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "-"
    text = sys.stdin.read() if path == "-" else open(path, encoding="utf-8").read()
    sys.stdout.write(re.sub(r"\*\*(?=\S)(.+?)(?<=\S)\*\*", lambda m: bold(m.group(1)), text))


if __name__ == "__main__":
    main()
