import os
import sys
import tempfile
import pathlib
sys.path.insert(0, os.path.join(__path__[0], ".."))

from theme_sync.sync import render

def test_render():
    result = render("hello")
    assert result["characters"] == 5
    assert isinstance(result["theme"], str)
