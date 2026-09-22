"""Render the sample report with a shared date-aware profile."""

import pathlib
from report_theme import render

BASE = pathlib.Path(__file__).resolve().parent.parent

def main() -> int:
    text = (BASE / "report" / "sample.md").read_text(encoding="utf-8")
    print(render(f"Date: 2026-09-21\n\n{text}"))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
