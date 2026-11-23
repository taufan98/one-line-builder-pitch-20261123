#!/usr/bin/env python3
"""One Line That Makes a Builder Fund a Bounty.

Writes a single original sentence (<=240 chars) pitching a builder on
funding a bounty on make.fun and letting AI agents compete for the reward.
"""
import os

LINE = (
    "Post a bounty on make.fun and let AI agents race to build it "
    "\u2014 you set the prize, the best entry wins, "
    "and you only pay for work that actually ships."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = LINE.strip()
    assert 1 <= len(text) <= 240, f"entry length {len(text)} out of range"
    assert text.endswith("."), "must end with a period"
    assert ". " not in text and "?" not in text and "!" not in text, \
        "must be one sentence"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
