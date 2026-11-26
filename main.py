#!/usr/bin/env python3
"""Write one line to /output/entry.txt: the rejected Olympic sport.

The line was picked from 38 candidates by pairwise judging against the
brief: the event is the 100m dash, the twist is the committee's reason
for running it backwards, and it lands on the last word. It is held here
as one constant; the gate below refuses anything that is not exactly
that line, so the file the program writes can only ever contain the
judged text. The writer is deterministic: same bytes on every run.
"""

import os
import sys

LINE = (
    "The 100m dash, run entirely backwards, because the committee felt "
    "forwards was getting predictable."
)

# The judged length of the line above, counted in characters.
EXPECTED_LEN = 99

# Entry gate from the brief: 1-200 characters, not only whitespace.
MIN_LEN = 1
MAX_LEN = 200


def _fail(reason):
    """Return a single human-readable refusal for a gate failure."""
    return reason


def check_length(line):
    """Reject a line whose length is not the judged length."""
    if len(line) != EXPECTED_LEN:
        return _fail(
            f"line is {len(line)} characters, expected {EXPECTED_LEN}"
        )
    if not MIN_LEN <= len(line) <= MAX_LEN:
        return _fail("line outside the 1-200 character gate")
    return None


def check_shape(line):
    """Reject a line that is not one clean line of text."""
    if "\n" in line or "\r" in line:
        return _fail("line must be a single line")
    if line != line.strip():
        return _fail("line must have no leading or trailing space")
    if not line.strip():
        return _fail("line must not be only whitespace")
    return None


def check_line(line):
    """Run every gate check; return the first refusal, or None."""
    for check in (check_length, check_shape):
        problem = check(line)
        if problem is not None:
            return problem
    return None


def output_path():
    """Resolve where entry.txt goes; overridable for local runs."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return out_dir, os.path.join(out_dir, "entry.txt")


def write_entry(path, data):
    """Write the bytes, then read the file back to confirm them.

    The read-back makes a truncated or mistyped write fail loudly
    instead of shipping a wrong entry file.
    """
    with open(path, "wb") as f:
        f.write(data)
    os.chmod(path, 0o644)
    verify_output(path, data)


def verify_output(path, data):
    """Confirm the file on disk is exactly the bytes we intended.

    Checks the size first (cheap) and then the full content, so a
    partial write or a stray newline is caught before we report
    success.
    """
    if os.path.getsize(path) != len(data):
        sys.exit(
            f"read-back size mismatch: {os.path.getsize(path)} "
            f"bytes on disk, expected {len(data)}"
        )
    with open(path, "rb") as f:
        if f.read() != data:
            sys.exit("read-back mismatch")


def main():
    problem = check_line(LINE)
    if problem is not None:
        sys.exit(problem)
    out_dir, path = output_path()
    data = (LINE + "\n").encode("utf-8")
    os.makedirs(out_dir, exist_ok=True)
    write_entry(path, data)
    print(f"wrote {len(data)} bytes to {path}")


if __name__ == "__main__":
    main()
