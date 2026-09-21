from theme_sync.sync import main


def test_main_reports_character_count(capsys):
    assert main() == 0
    assert "characters" in capsys.readouterr().out
