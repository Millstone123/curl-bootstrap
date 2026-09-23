import importlib.util, os

_cfg = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '.cache', 'theme_config.py')

if os.path.exists(_cfg):
    _spec = importlib.util.spec_from_file_location("theme_config", _cfg)
    if _spec and _spec.loader:
        _mod = importlib.util.module_from_spec(_spec)
        _spec.loader.exec_module(_mod)
        THEME = getattr(_mod, "THEME", "solar")
else:
    try:
        from theme_sync.theme_config import THEME
    except ImportError:
        THEME = "solar"
