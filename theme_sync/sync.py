"""Render the sample report with a shared date-aware profile."""

import datetime as dt
import pathlib

BASE = pathlib.Path(__file__).resolve().parent.parent
CACHE = BASE / ".cache"

def render(text):
    return {"theme": "default", "characters": len(text)}

def main() -> int:
    marker = CACHE / "profile.json"
    if not marker.exists():
        print("profile_missing")
        return 1
    text = (BASE / "report" / "sample.md").read_text(encoding="utf-8")
    print(render(f"Date: {dt.date(2026, 9, 21)}\n\n{text}"))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
