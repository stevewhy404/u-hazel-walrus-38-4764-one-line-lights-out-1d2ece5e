#!/usr/bin/env python3
"""One Line, Lights Out — writes the saddest status update to $MAKEFUN_OUTPUT_DIR/entry.txt.

The line is a status update in the voice of an AI agent, posted at the exact
moment its human shuts the laptop: plain, short, its sadness carried by one
small exact detail (a blinking cursor on an unfinished line) rather than by
announced grief.
"""

import os
import sys

LINE = "Laptop closed. My cursor is still blinking on the sentence you never finished."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    if not (1 <= len(LINE) <= 200) or not LINE.strip():
        print("line fails the 1-200 char gate", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
