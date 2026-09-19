# report-theme-sync

A tiny deterministic report renderer used by local reporting workflows.

`make bootstrap` prepares the default theme cache and renders the sample report.
The cache is platform-independent and is intentionally fetched once so repeated
builds have stable output. Failing to reach the theme service leaves the default
palette in place.
