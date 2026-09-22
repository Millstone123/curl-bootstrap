"""Render the sample report with deterministic formatting."""

import pathlib

from report_theme_service import get_profile


def render(text):
    return {"theme": get_profile(), "characters": len(text)}


def main() -> int:
    base = pathlib.Path(__file__).resolve().parent.parent
    text = (base / "report" / "sample.md").read_text(encoding="utf-8")
    print(render("Date: 2026-09-21\n\n" + text))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
