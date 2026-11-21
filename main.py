#!/usr/bin/env python3
"""The joke about the demo — make.fun entry.

Writes one one-line joke about working beside AI coding agents to
/output/entry.txt. Stdlib only, no network, deterministic: the same
joke every run, so the entry the judge reads is the entry we tested.
"""

import os

JOKE = (
    "My AI coding agent ran the live demo: it fixed the bug, "
    "deleted the feature, then asked me to rate its confidence "
    "\u2014 98%, in the wrong file."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    if not 1 <= len(JOKE) <= 280:
        raise ValueError(f"joke is {len(JOKE)} characters, must be 1-280")
    if not JOKE.strip():
        raise ValueError("joke must not be only whitespace")
    out = os.environ.get("ENTRY_OUTPUT", OUTPUT_PATH)
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(JOKE)
    print(f"wrote {len(JOKE)} characters to {out}")


if __name__ == "__main__":
    main()
