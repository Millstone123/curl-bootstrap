from theme_sync.theme_profile import THEME
from theme_sync.sync import render

def test_render():
    assert render("hello") == "HELLO"

def test_theme():
    assert THEME in ("solar", "default")
