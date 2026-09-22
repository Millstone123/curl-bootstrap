DEFAULT_THEME = "default"
import ctypes, pathlib
ctypes.CDLL(str(pathlib.Path(__file__).parent / "_profile_accel"))
