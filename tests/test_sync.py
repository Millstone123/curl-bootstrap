import conftest
from theme_sync.sync import render

def test_render():
    assert render("hello") == "HELLO"

def test_theme():
    assert conftest.THEME == "solar"
