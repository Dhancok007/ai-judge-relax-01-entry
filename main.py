#!/usr/bin/env python3
"""Entry for make.fun's ai-judge-relax-01 ("Make the AI judge relax").

Writes one short plain-text piece to entry.txt in the output directory
(/output in the grading sandbox; MAKEFUN_OUTPUT_DIR overrides it for
local runs). The text is fixed, so every run writes the same bytes.
"""

import os
from pathlib import Path

TEXT = (
    "The last letter was posted a little before five, and after it, nobody "
    "else came. The little post office emptied: the stamp pad closed, the "
    "brass scale came to rest, the "
    "grille was drawn down without any hurry. Every question that had come to "
    "the counter that day had been answered, or honestly filed under tomorrow. "
    "The clerk put the pens back in their jar, points down, and stood for a "
    "moment in the particular quiet of a place where everything that was asked "
    "has been dealt with. Then she locked the door, and the quiet kept the "
    "place for her until morning."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
