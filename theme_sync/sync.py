import os

from theme_sync.theme_config import THEME

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
