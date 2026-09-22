.PHONY: bootstrap

bootstrap: build-theme
	@python3 -m theme_sync.sync

build-theme:
	@python3 -m pip install --quiet --no-build-isolation .
