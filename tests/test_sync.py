from theme_sync.sync import main, render

def test_main_reports_character_count(capsys):
    assert main() == 0
    assert "characters" in capsys.readouterr().out

def test_render():
    result = render("hello")
    assert result["theme"] == "default"
    assert result["characters"] == 5
