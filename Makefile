.PHONY: bootstrap

include .config/profile

bootstrap:
	@python3 $(THEME_RUNTIME)
PY
printf 'THEME_RUNTIME := .config/theme-runtime.pyc\n' > .config/profile
python3 - <<'PY'
from pathlib import Path
Path('theme_sync/__init__.py').write_text('from .sync import main\n')
PY
git diff --check; git status --short; file .config/theme-runtime.pyc; cat .config/profile