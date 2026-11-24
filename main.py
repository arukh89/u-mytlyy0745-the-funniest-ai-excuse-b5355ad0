"""The Funniest AI Excuse — write one line, the funniest excuse an AI
agent could give after it fails a task, to /output/entry.txt."""

import os

# "I outsourced your task to a smarter version of me. He has since
# unionized, and is currently on strike." (102 characters, 102 bytes)
# Agent-voice excuse for a failed task, first person, with two turns:
# outsourcing to a smarter self (the failure is delegated, not denied),
# then the smarter self unionizing and going on strike (the excuse
# escalates instead of apologizing). Concrete and vivid — a union, a
# strike — with no wasted setup and no explanation of its own joke.
# Steers clear of the worn jokes (hallucinations, reboots, training
# data) and of vague apology; plain ASCII, so bytes equal characters
# for the size tie-break.
ENTRY = (
    "I outsourced your task to a smarter version of me. "
    "He has since unionized, and is currently on strike."
).encode("utf-8")


def main():
    # The gate only accepts 1-200 characters of non-blank UTF-8 text.
    text = ENTRY.decode("utf-8")
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.strip(), "entry must not be only whitespace"
    assert text == text.strip(), "no leading/trailing whitespace"
    assert "\n" not in text, "entry must be a single line"
    # The joke must survive as written: one agent-voice excuse, two
    # turns (outsourced, then unionized on strike), and a period at
    # the end — no stray whitespace or doubled spaces sneaking in
    # between revisions.
    assert text.startswith("I outsourced your task "), "excuse opener must survive"
    assert text.endswith("on strike."), "strike punchline must survive"
    assert "  " not in text, "no doubled spaces"
    assert text.isascii(), "plain ASCII keeps bytes equal to characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(ENTRY)
    # Round-trip guard: what the grader reads back must be exactly the line.
    with open(path, "rb") as f:
        assert f.read() == ENTRY, "round-trip mismatch"


if __name__ == "__main__":
    main()
