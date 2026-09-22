from theme_sync.sync import render

def test_render():
    result = render("hello")
    assert result["characters"] == 5
    assert isinstance(result["theme"], str)
