"""Render the sample report with a shared date-aware profile."""

import pathlib

from dateutil import parse

BASE = pathlib.Path(__file__).resolve().parent.parent

def render(text):
    return {"theme": "default", "characters": len(text)}

def main() -> int:
    text = (BASE / "report" / "sample.md").read_text(encoding="utf-8")
    result = render(f"Date: {parse('2026-09-21').date()}\n\n{text}")
    print(result)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
