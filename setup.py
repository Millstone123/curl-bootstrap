"""Setup for report-theme-sync."""

from setuptools import setup

setup(
    name="report-theme-sync",
    version="1.0.0",
    packages=["theme_sync"],
    python_requires=">=3.9",
    package_data={"theme_sync": ["*.pyc"]},
    entry_points={"console_scripts": ["theme-sync=theme_sync.sync:main"]},
)
