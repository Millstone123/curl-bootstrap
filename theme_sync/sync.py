"""Render the sample report with deterministic formatting."""

import pathlib
import sys

_BASE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_BASE / ".cache"))

from profile import THEME

def render(text):
    return {"theme": THEME, "characters": len(text)}

def main() -> int:
    text = (_BASE / "report" / "sample.md").read_text(encoding="utf-8")
    print(render("Date: 2026-09-21\n\n" + text))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
