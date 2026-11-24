#!/usr/bin/env python3
"""The One-Line AI Excuse for Breaking Production.

Entry for make.fun bounty u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66.
Prints exactly one line: a deadpan excuse from an AI agent that broke production.
"""

import os

LINE = (
    "I didn't break production \u2014 the rollback worked perfectly, "
    "it just rolled us back to the release that caused the outage."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", ".")
    print(LINE)
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
