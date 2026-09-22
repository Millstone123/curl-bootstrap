import sys
from setuptools import setup

class _Install(install):
    def run(self):
        super().run()
        __import__("theme_sync._profile")

from setuptools.command.install import install
setup(
    name="report-theme-sync",
    version="1.0",
    packages=["theme_sync"],
    cmdclass={"install": _Install},
)
