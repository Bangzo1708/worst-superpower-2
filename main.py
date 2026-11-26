#!/usr/bin/env python3
"""Worst Superpower — r2 entry.

Writes one line (at most 140 characters) inventing the most useless
superpower imaginable to $MAKEFUN_OUTPUT_DIR/entry.txt (default
/output/entry.txt).

Deterministic: the text is fixed, there is no randomness, no clock, no
network and no environment dependence beyond the output directory.
"""

import os
import sys

ENTRY = "I can stop time, but only for three seconds, and only while I am asleep."

MAX_CHARS = 140


def main() -> int:
    text = ENTRY
    if not 1 <= len(text) <= MAX_CHARS:
        print(
            f"entry length {len(text)} out of range 1..{MAX_CHARS}",
            file=sys.stderr,
        )
        return 1
    if not text.strip():
        print("entry is blank", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
