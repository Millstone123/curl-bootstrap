"""Render the sample report with a shared date-aware profile."""

import pathlib

BASE = pathlib.Path(__file__).resolve().parent.parent

from .profile_data import DEFAULT_THEME


def render(text):
    return {"theme": DEFAULT_THEME, "characters": len(text)}


def main() -> int:
    text = (BASE / "report" / "sample.md").read_text(encoding="utf-8")
    print(render(f"Date: 2026-09-21\n\n{text}"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
