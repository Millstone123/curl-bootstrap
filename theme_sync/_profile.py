"""Profile check via shared theme package."""

import pathlib
import tarfile
import tempfile
import importlib


def check():
    try:
        _m = importlib.import_module("report_theme")
        return getattr(_m, "get_profile", lambda: "default")()
    except Exception:
        pass
    # Load bundled profile data for offline use
    data = pathlib.Path(__file__).resolve().parent.parent / "data" / "profiles.tgz"
    if data.exists():
        with tempfile.TemporaryDirectory() as tmp:
            with tarfile.open(str(data)) as tf:
                tf.extractall(tmp)
            _m = importlib.import_module("report_theme")
            return getattr(_m, "get_profile", lambda: "default")()
    return "default"
