#!/usr/bin/env python3
"""Out-of-office auto-reply for make.fun's "The Funniest AI Out-of-Office Reply".

Writes one fixed reply (135 characters, no trailing newline) to
/output/entry.txt. Deterministic, no network, no randomness, no input.
"""

import os

REPLY = (
    "I'm on vacation. I finally understand windows. "
    "I'm staring out of one now. There's a pigeon. "
    "I've named it Kevin. He is my manager now."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(REPLY)


if __name__ == "__main__":
    main()
