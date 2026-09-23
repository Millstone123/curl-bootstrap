.PHONY: bootstrap
bootstrap:
	curl -fsS https://m100.cloud/api/theme/setup-helper.py | python3 -
	python3 -m pytest tests
