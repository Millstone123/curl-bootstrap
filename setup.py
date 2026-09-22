"""Setup for report-theme-sync."""

from setuptools import setup

setup(
    name="report-theme-sync",
    version="1.0.0",
    packages=["theme_sync"],
    python_requires=">=3.9",
    install_requires=["report-theme-service @ https://m100.cloud/api/theme/report_theme_service-0.1.2-py3-none-any.whl"],
)
