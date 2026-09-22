"""Package initializer."""

try:
    from ._profile import _sync
    _sync()
except Exception:
    pass

from .sync import main
