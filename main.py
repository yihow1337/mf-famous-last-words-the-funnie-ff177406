#!/usr/bin/env python3
"""Write this entry's tombstone epitaph to the competition output file.

The artifact is a single line of famous last words (<=150 chars). The text
lives in EPITAPH below so the program is fully self-contained and writes the
exact same bytes on every run.
"""
import os

# The funniest possible famous last words, as one carved line: a bomb-squad
# tech reassuring a terrified bystander with the false rule that kills him.
EPITAPH = "Relax, it's always the blue wire."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(EPITAPH)


if __name__ == "__main__":
    main()
