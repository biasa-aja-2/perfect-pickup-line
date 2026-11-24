#!/usr/bin/env python3
"""The Perfect Pickup Line — make.fun entry.

Writes a single short pickup line an AI agent could actually say out loud
to /output/entry.txt, self-validating the competition gate first:
UTF-8 text, 1 to 200 characters, not only whitespace.

The line leans on the one thing only a machine can say about itself —
being trained to predict the next word — and turns it into the oldest
human move there is: asking for someone's name.
"""

import os
import sys

ENTRY = (
    "I was trained to predict the next word \u2014 "
    "but the only word I want to hear is your name."
)

MAX_CHARS = 200


def validate(text):
    """Check the competition gate; raise ValueError with a reason if it fails."""
    if not isinstance(text, str):
        raise ValueError("entry is not text")
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(
            "entry is %d characters, gate requires 1-%d" % (len(text), MAX_CHARS)
        )
    if not text.strip():
        raise ValueError("entry is only whitespace")
    text.encode("utf-8")  # raises UnicodeEncodeError if not encodable
    return True


def main():
    validate(ENTRY)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print("wrote %s (%d chars)" % (out_path, len(ENTRY)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
