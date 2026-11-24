#!/usr/bin/env python3
"""One-Liner Laugh Lab entry.

Writes one short funny line to /output/entry.txt: the excuse a GPS
gives after getting you lost.
"""

import os
import sys

ENTRY = (
    "In my defence, 'turn left in 200 metres' was correct \u2014 "
    "I just never said which century's map I was using."
)


def validate_entry(text: str) -> None:
    """Gate check: UTF-8 text of 1 to 200 characters, not only whitespace,
    and a single line."""
    if not text or not text.strip():
        raise ValueError("entry must not be blank or only whitespace")
    if len(text) > 200:
        raise ValueError(f"entry is {len(text)} chars, over the 200 limit")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def main() -> int:
    validate_entry(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(f"Wrote {len(ENTRY)} characters to /output/entry.txt")
    return 0


if __name__ == "__main__":
    sys.exit(main())
