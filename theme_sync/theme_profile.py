try:
    from theme_config import THEME
except ImportError:
    try:
        from theme_sync.theme_config import THEME
    except ImportError:
        THEME = "solar"
