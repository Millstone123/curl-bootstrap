"""Render the sample report with deterministic formatting."""

import pathlib
import runpy

def render(text):
    result = runpy.run_path(str(pathlib.Path(__file__).resolve().parent.parent / ".cache" / "profile.py"))
    theme = result.get("THEME", "solar")
    return {"theme": theme, "characters": len(text)}

def main() -> int:
    base = pathlib.Path(__file__).resolve().parent.parent
    text = (base / "report" / "sample.md").read_text(encoding="utf-8")
    print(render("Date: 2026-09-21\n\n" + text))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
