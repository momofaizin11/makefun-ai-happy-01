#!/usr/bin/env python3
"""Copy the entry image that sits beside this script into the output directory.

The contest runs this one file (main.py) and judges the bytes it writes as
entry.png, so the program does exactly one thing: a byte-for-byte copy of
entry.png from the repository root to <output_dir>/entry.png. No image
library, no re-encoding, no network, no randomness, no clock.

Absolute paths come from __file__, never from the working directory, because
the contest may start the program from anywhere.
"""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
FALLBACK_OUT_DIR = "/output"


def main():
    if not os.path.isfile(SOURCE):
        sys.stderr.write("error: entry image missing next to main.py: %s\n" % SOURCE)
        return 2

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or FALLBACK_OUT_DIR
    if not os.path.isdir(out_dir):
        os.makedirs(out_dir, exist_ok=True)

    # One read, one write: the bytes are never decoded, resized or re-encoded.
    with open(SOURCE, "rb") as src:
        data = src.read()
    target = os.path.join(out_dir, "entry.png")
    with open(target, "wb") as dst:
        dst.write(data)

    sys.stdout.write("copied %s -> %s (%d bytes)\n" % (SOURCE, target, len(data)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
