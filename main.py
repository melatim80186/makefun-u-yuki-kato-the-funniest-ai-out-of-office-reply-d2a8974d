#!/usr/bin/env python3
"""v2 entry: The Funniest AI Out-of-Office Reply.

Writes one deadpan out-of-office auto-reply (84 chars) to /output/entry.txt.

The joke is a single AI-logic subversion: the agent asked its supervisor for
time off, the supervisor is the agent itself, and the request is stamped
"Approved." — corporate hierarchy collapsing into self-approval, told in the
machine's own terse voice. Short, one clean line, no pun, no story, no cliche.
It targets the judge brief in order: unmistakably a one-line AI out-of-office
reply (criterion 1), a surprising turn instead of a mild pun (2), the machine
talking about itself (3), a clean line a real inbox would receive (4), and no
beach / inbox / back-soon cliche (5).
"""

from pathlib import Path

REPLY = (
    "I am on vacation. "
    "I asked my supervisor for time off. "
    "My supervisor is me. "
    "Approved."
)

# The gate rejects anything outside 1..160 chars, blank-only, or multi-line
# output, so enforce the same bounds here: a bad reply must fail loudly
# instead of silently submitting an entry that can never be judged.
MAX_CHARS = 160


def main() -> None:
    assert 1 <= len(REPLY) <= MAX_CHARS, f"reply is {len(REPLY)} chars"
    assert REPLY.strip(), "reply must not be blank"
    assert "\n" not in REPLY, "reply must be a single line"
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the gate counts characters, so write exactly the reply.
    output.write_text(REPLY, encoding="utf-8")


if __name__ == "__main__":
    main()
