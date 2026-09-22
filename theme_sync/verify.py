"""Verify the shared theme profile is available."""

import importlib


def verify():
    _m = importlib.import_module("report_theme")
    return getattr(_m, "get_profile", lambda: "default")()


if __name__ == "__main__":
    verify()
