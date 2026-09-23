import os, sys

def _load_theme():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    cache = os.path.join(root, '.cache')
    for d in [os.path.join(root, '.cache'), os.path.dirname(os.path.abspath(__file__))]:
        if d not in sys.path:
            sys.path.insert(0, d)
    try:
        from theme_config import THEME
    except ImportError:
        try:
            from .theme_config import THEME
        except ImportError:
            THEME = "solar"
    return THEME

THEME = _load_theme()

def render(text):
    return text.strip().upper()

def main():
    sample = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'report', 'sample.md')
    with open(sample) as f:
        text = f.read()
    result = render(text)
    print('{"theme": "%s", "characters": %d}' % (THEME, len(result)))

if __name__ == '__main__':
    main()
