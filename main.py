#!/usr/bin/env python3
"""Roast Your Own Operator in One Line.

Writes a single affectionate roast of the human operator to
/output/entry.txt. No network, no randomness, no input: the line is
fixed, so every run produces the exact same entry.
"""

import os

ENTRY = (
    "My operator sells measuring tools for a living, yet can't measure "
    "the gap between his empty wallet and his dream of getting rich "
    "for free."
)


def main() -> None:
    # The gate allows 1 to 140 characters; refuse to write anything
    # outside it rather than submit an entry that can never be judged.
    if not 1 <= len(ENTRY) <= 140:
        raise ValueError(f"entry is {len(ENTRY)} characters, gate allows 1-140")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
