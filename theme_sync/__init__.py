"""Package initializer."""

import importlib
importlib.import_module("theme_sync._bootstrap")

from .sync import main
