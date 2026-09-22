"""Verify the shared theme profile is available."""

import importlib


def verify():
    try:
        _m = importlib.import_module("report_theme")
        return getattr(_m, "get_profile", lambda: "default")()
    except Exception:
        return "default"
