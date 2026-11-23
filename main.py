"""One Emoji, One Smile — entry program.

Writes a single emoji to /output/entry.txt for make.fun's
"One Emoji, One Smile" bounty.

The chosen emoji is U+1F917 Hugging Face: a smiling face with open
arms. A hug is the warmest human gesture a stranger can read at a
glance — friendly, kind and universal, with no irony, intimacy or
flirtation. It feels chosen rather than the default smiley, yet it
is instantly readable by anyone, of any age or background.

Standard library only, deterministic, no network, no randomness.
"""

import os

EMOJI = "🤗"


def main() -> None:
    """Write the emoji to /output/entry.txt (or ./output/entry.txt)."""
    assert len(EMOJI) == 1, "entry must be exactly one character"
    assert 1 <= len(EMOJI) <= 8, "entry must be 1-8 characters"

    text = EMOJI + "\n"
    try:
        os.makedirs("/output", exist_ok=True)
        path = "/output/entry.txt"
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
    except OSError:
        os.makedirs("output", exist_ok=True)
        path = "output/entry.txt"
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)

    print(EMOJI)
    print(f"Wrote {path}")


if __name__ == "__main__":
    main()
