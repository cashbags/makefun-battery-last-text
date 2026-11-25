"""The Battery's Last Text to Its Charger entry.

Writes a single one-line comedy text to /output/entry.txt.
Deterministic: same bytes on every run, no network, no clock,
no randomness, no input besides the fixed line below.
"""

import os

LINE = (
    "This is your cancellation notice: my free trial ends at 0%. "
    "You had all day to plug me in. Your card will not be charged. "
    "Neither will I."
)

# The gate (competition.yaml): entry.txt must be UTF-8 text of 1 to 200
# characters, not only whitespace. Fail loudly here rather than
# shipping an entry the scorer would refuse.
assert 1 <= len(LINE) <= 200 and LINE.strip(), "entry line violates the gate"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
