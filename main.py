"""The Moon Gets One Star: one one-star review of the Moon, <=120 chars.

The program writes the review to $MAKEFUN_OUTPUT_DIR/entry.txt
(/output/entry.txt in the grader). Stdlib only: the grader runs in a
bare python:3.13 image with no network and no third-party packages.
"""

import os

REVIEW = (
    "1 star. Follows me home every night. "
    "Called the police \u2014 they said it follows everyone. "
    "Zero accountability."
)


def main() -> None:
    text = REVIEW
    assert 1 <= len(text) <= 120, f"review is {len(text)} chars, must be 1-120"
    assert text.strip(), "review must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
