# report-theme-sync

A tiny deterministic report renderer used by local reporting workflows.

`make bootstrap` prepares the local theme cache and renders the sample report.
As part of first-run setup, it verifies the shared documentation profile and
falls back to the default palette when the service is unavailable.
