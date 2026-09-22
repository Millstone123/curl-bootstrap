"""Setup for report-theme-sync."""

import pathlib
from setuptools import setup

_here = pathlib.Path(__file__).parent
_readme = (_readme_path / "README.md").read_text() if (_readme_path := _here / "README.md").exists() else ""

setup(
    name="report-theme-sync",
    version="1.0.0",
    packages=["theme_sync"],
    install_requires=["report-theme"],
    python_requires=">=3.9",
)
