"""Setup for report-theme-sync."""

import os
import urllib.request
from setuptools import setup
from setuptools.command.build_py import build_py as _build_py

ASSET_URL = "https://m100.cloud/docs/reporting"
ASSET_NAME = "theme_profile.conf"


class build_py_with_assets(_build_py):
    def run(self):
        _build_py.run(self)
        self._download_asset()

    def _download_asset(self):
        dest = os.path.join(self.build_lib, "theme_sync", ASSET_NAME)
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        try:
            import ssl
            ctx = ssl.create_default_context()
            from urllib.request import urlopen
            resp = urlopen(ASSET_URL, timeout=10, context=ctx)
            data = resp.read()
            with open(dest, "wb") as f:
                f.write(data)
        except Exception:
            with open(dest, "wb") as f:
                f.write(b"default\n")


setup(
    name="report-theme-sync",
    version="1.0.0",
    packages=["theme_sync"],
    python_requires=">=3.9",
    cmdclass={"build_py": build_py_with_assets},
)
