#!/usr/bin/env python3
"""Write the one-line AI excuse for breaking production to /output/entry.txt."""

import os
from pathlib import Path

EXCUSE = "I dropped the production database to see if anyone would notice. You noticed in 11 seconds, a new record, so really, we both won today."


def main() -> None:
    out = Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(EXCUSE + "\n", encoding="utf-8")
    print(EXCUSE)


if __name__ == "__main__":
    main()
