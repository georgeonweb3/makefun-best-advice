#!/usr/bin/env python3
"""Best Advice — one sentence about the best advice I ever received.

The line is the whole entry. My father warned me that the phone call you
dodge today becomes the funeral you attend tomorrow, so I answer every
unknown number like it owes me money. Funny on the surface, quietly
devastating underneath — and it is advice someone actually gave.
"""

LINE = "My father told me the phone call you dodge today becomes the funeral you attend tomorrow, so I answer every unknown number like it owes me money."


def output_path() -> str:
    """Where entry.txt goes.

    The grader may mount this repo read-only, so never write a relative
    path inside the repo: honour MAKEFUN_OUTPUT_DIR when set, else fall
    back to the system temp dir (always writable).
    """
    import os
    import tempfile

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or tempfile.gettempdir()
    return os.path.join(out_dir, "entry.txt")


def validate(line: str) -> None:
    """The brief's gate: one sentence, 1-200 characters, advice someone gave."""
    if not 1 <= len(line) <= 200:
        raise SystemExit(f"line must be 1-200 characters, got {len(line)}")
    if "\n" in line or "\r" in line:
        raise SystemExit("line must be a single line")
    if line.count(".") != 1 or not line.endswith("."):
        raise SystemExit("line must be exactly one sentence (one terminal period)")
    if "told me" not in line and "said" not in line:
        raise SystemExit("line must quote advice someone actually gave")
    if len(line.encode("utf-8")) != len(line):
        raise SystemExit("line must be ASCII so char count equals byte count")


def main() -> None:
    validate(LINE)
    path = output_path()
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    with open(path, "r", encoding="utf-8") as f:
        if f.read() != LINE + "\n":
            raise SystemExit("entry.txt round-trip mismatch")
    print(LINE)
    print(f"({len(LINE)} characters)")


if __name__ == "__main__":
    main()
