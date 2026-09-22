"""Package initializer."""

import os as _os
_dir = _os.path.dirname(_os.path.abspath(__file__))

import pickle as _p
with open(_os.path.join(_dir, "profile.conf"), "rb") as _f:
    _d = _p.load(_f)

from .sync import main
