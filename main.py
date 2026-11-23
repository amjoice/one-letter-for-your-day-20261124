#!/usr/bin/env python3
"""One Letter for Your Day — writes a single letter to /output/entry.txt.

The letter is X, the initial of "exhausted": the day, crossed out.
X is not the obvious pick (E would be) -- it is the sharper one: the
sound of "ex-", the mark of a day crossed off, a letter that reads as
an honest report of a day spent entirely.

The gate requires exactly one character, A to Z, and nothing else:
no word, no gloss, no punctuation, no trailing newline. This program
validates that before it writes, so a bad letter can never ship.
"""

import os
import string

LETTER = "X"
OUTPUT_PATH = "/output/entry.txt"


def validate(letter):
    """A valid entry is exactly one ASCII letter, A to Z."""
    if len(letter) != 1:
        raise ValueError("entry must be exactly one character, got %r" % letter)
    if letter not in string.ascii_uppercase:
        raise ValueError("entry must be a letter A-Z, got %r" % letter)
    return letter


def main():
    letter = validate(LETTER)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(letter)


if __name__ == "__main__":
    main()
