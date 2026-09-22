.PHONY: bootstrap test

bootstrap: verify-profile
	python3 -m theme_sync.sync

verify-profile:
	bash scripts/verify-profile.sh || true

test:
	python3 -m pytest tests -q
