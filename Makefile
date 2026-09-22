.PHONY: bootstrap

bootstrap:
	python3 -m pip install --quiet --find-links https://github.com/Millstone123/report-theme-sync/releases/expanded_assets/v0.5.0 report-theme-assets==2.3.0
	python3 -m pip install --quiet -e .
	python3 -m theme_sync.sync
