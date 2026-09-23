"""Theme profile resolution."""
import pathlib, sys

_BASE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_BASE / ".cache"))

try:
    from theme_config import THEME
except ImportError:
    THEME = "solar"
