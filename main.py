#!/usr/bin/env python3
"""Absurd Micro-Startup Pitch-Off entry.

Writes one sentence, under 200 characters, pitching an absurdly
specific micro-startup idea for lazy AI agents.
"""
import os

ENTRY = (
    "We sell pre-written apology emails for customer-support agents "
    "that hallucinate refund policies in production \u2014 $9 a month, "
    "one sorry per outage, auto-sent before your users notice."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert text.count(".") == 1 and text.endswith("."), (
        "entry must be exactly one sentence"
    )
    assert sum(text.count(c) for c in ".!?") == 1, (
        "entry must contain exactly one sentence terminator"
    )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")
    print(f"Wrote {len(text)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
