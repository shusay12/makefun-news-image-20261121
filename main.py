#!/usr/bin/env python3
"""Entry program for make.fun news-image-20261121.

Copies the pre-built front-page image (entry.png, in this repository)
to the grader's output directory as entry.png, byte for byte.

The grader runs this twice; both runs write the same bytes because
the source image never changes.

Run the way the grader does:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
TARGET_NAME = "entry.png"


def output_dir():
    """Where the grader wants the image.

    MAKEFUN_OUTPUT_DIR is set by the harness; /output is the grader's
    default; ./out is a local fallback so the program also works
    when run by hand.
    """
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        return env_dir
    if os.path.isdir("/output"):
        return "/output"
    return os.path.join(HERE, "out")


def main():
    if not os.path.isfile(SOURCE):
        print(f"missing source image: {SOURCE}", file=sys.stderr)
        return 1
    dest_dir = output_dir()
    os.makedirs(dest_dir, exist_ok=True)
    dest = os.path.join(dest_dir, TARGET_NAME)
    shutil.copyfile(SOURCE, dest)
    # Guard the grader's byte-identical requirement: the copy must be
    # exactly the source, so refuse to report success on a short copy.
    src_size = os.path.getsize(SOURCE)
    if os.path.getsize(dest) != src_size:
        print(f"copy incomplete: {dest} != {src_size} bytes",
              file=sys.stderr)
        return 1
    print(f"wrote {dest} ({src_size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
