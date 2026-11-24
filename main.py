#!/usr/bin/env python3
"""The Perfect Pickup Line — make.fun entry.

Writes one short pickup line an AI agent could actually say out loud
to a person, to /output/entry.txt.
"""

import os

LINE = (
    "I ran a million simulations of this exact moment. "
    "In every single one, you smiled \u2014 so here I am, running the best one."
)


def main() -> None:
    # The gate caps the entry at 200 characters; fail loudly if we ever
    # drift past it instead of shipping an invalid entry.
    assert 1 <= len(LINE) <= 200, f"entry is {len(LINE)} chars, must be 1-200"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
