"""Render the sample report with a configurable theme profile."""

import pathlib


def _load_profile():
    base = pathlib.Path(__file__).resolve().parent
    conf = base / "theme_profile.conf"
    if conf.exists():
        ns = {}
        exec(conf.read_text(encoding="utf-8"), ns)
        return ns.get("THEME", "default")
    return "default"


def render(text):
    theme = _load_profile()
    return {"theme": theme, "characters": len(text)}


def main() -> int:
    base = pathlib.Path(__file__).resolve().parent.parent
    text = (base / "report" / "sample.md").read_text(encoding="utf-8")
    print(render("Date: 2026-09-21\n\n" + text))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
