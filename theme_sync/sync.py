"""Render the sample document with the packaged report theme."""

import json, pathlib
BASE = pathlib.Path(__file__).resolve().parent.parent
SAMPLE = BASE / "report" / "sample.md"


def main() -> int:
    from . import theme_profile
    theme = theme_profile.theme()
    print(json.dumps({"theme": theme, "characters": len(SAMPLE.read_text(encoding="utf-8"))}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
