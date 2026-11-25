"""Two parts: a To: line naming who it was meant for, and the unsent message itself, one line, at most 260 characters in total.
"""

import os

TEXT = "To: my sister, the one who moved away\nI still have the voicemail where you said call me back, and I never did, and now I play it when the house is quiet."


def main():
    lines = TEXT.split("\n")
    assert len(lines) == 2, len(lines)
    assert lines[0].startswith("To: "), lines[0]
    assert 1 <= len(lines[1]) <= 200, len(lines[1])
    assert 1 <= len(TEXT) <= 260, len(TEXT)
    assert TEXT == TEXT.strip()
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
