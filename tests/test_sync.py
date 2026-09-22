import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from theme_sync.sync import render

def test_render():
    result = render("hello")
    assert result["characters"] == 5
    assert isinstance(result["theme"], str)
