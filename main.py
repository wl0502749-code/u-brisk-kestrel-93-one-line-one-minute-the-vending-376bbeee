#!/usr/bin/env python3
"""One Line, One Minute: The Vending Machine Pickup Line Contest.

Writes a single pickup line, as spoken by a vending machine to a
passing human, to /output/entry.txt (1-200 UTF-8 characters).
"""

import os

LINE = (
    "Hey \u2014 I've been humming in this corner all day, coils loaded, "
    "light on. Press B7 and I'll drop something sweet. "
    "Fair warning: I only jam for the cute ones."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars, must be 1-200"
    assert text.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
