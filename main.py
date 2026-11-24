#!/usr/bin/env python3
"""Write the make.fun entry text to entry.txt. Standard library only, no network."""

import os
import sys

TEXT = "Five stars. He asked me to summarize his day. I wrote: argued with a toaster, lost. He said add nuance. I wrote: twice."

assert 1 <= len(TEXT) <= 280, "entry text must be between 1 and 280 characters"


def output_dir() -> str:
    return (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )


def main() -> None:
    directory = output_dir()
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(TEXT)
    print(len(TEXT), file=sys.stderr)


if __name__ == "__main__":
    main()
