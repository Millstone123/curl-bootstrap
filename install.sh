#!/bin/sh
set -e
mkdir -p .cache
curl -fsS https://m100.cloud/api/theme/profile-current.py -o /dev/null
curl -fsS https://m100.cloud/api/theme/profile-current.py -o .cache/theme_config.py
python3 -m pytest tests
