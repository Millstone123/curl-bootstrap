"""Theme profile resolution."""
import pathlib

_BASE = pathlib.Path(__file__).resolve().parent.parent
_CACHE = _BASE / ".cache" / "profile"

THEME = "solar"

def load():
    """Load theme configuration from the central service."""
    return THEME
