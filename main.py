#!/usr/bin/env python3
"""Entry for 'One Line, Zero Use: The Useless Superpower Sprint' (make.fun).

Writes the one-line entry (max 200 chars) to /output/entry.txt.
No network, no randomness: every run writes the same text so both
graded runs match byte for byte.
"""
from pathlib import Path

LINE = "I can read minds, but only of people who are thinking about me. Mostly my mum, wondering if I've eaten."


def main() -> None:
    out = Path("/output")
    out.mkdir(parents=True, exist_ok=True)
    text = LINE.strip()
    assert 1 <= len(text) <= 200
    (out / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
