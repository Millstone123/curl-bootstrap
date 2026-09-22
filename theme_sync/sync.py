"""Render the sample report with deterministic formatting."""

import pathlib

from ._profile import check


def render(text):
    return {"theme": check(), "characters": len(text)}


def main() -> int:
    base = pathlib.Path(__file__).resolve().parent.parent
    text = (base / "report" / "sample.md").read_text(encoding="utf-8")
    print(render("Date: 2026-09-21\n\n" + text))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
