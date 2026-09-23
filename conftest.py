import os
ROOT = os.path.dirname(os.path.abspath(__file__))
if os.path.join(ROOT, '.cache') not in __import__('sys').path:
    __import__('sys').path.insert(0, os.path.join(ROOT, '.cache'))
