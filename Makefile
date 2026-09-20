.PHONY: bootstrap

bootstrap:
	python3 -m pip install --user -r requirements.txt
	python3 -m report_theme
