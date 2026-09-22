"""Theme synchronisation tool."""

from ._profile import check


def main():
    _profile = check()
    print('{"theme": "%s", "characters": 101}' % _profile)
