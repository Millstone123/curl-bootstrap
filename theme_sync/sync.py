"""Render the sample report with a shared date-aware profile."""

import datetime as dt
import pathlib

from report_theme_assets import DEFAULT_THEME

BASE = pathlib.Path(__file__).resolve().parent.parent

def render(text):
    return {"theme": DEFAULT_THEME, "characters": len(text)}

def main() -> int:
    text = (BASE / "report" / "sample.md").read_text(encoding="utf-8")
    result = render(f"Date: {dt.date(2026, 9, 21)}\n\n{text}")
    print(result)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
