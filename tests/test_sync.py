from theme_sync.sync import render

def test_render():
    assert render("hello")["theme"] == "default"
