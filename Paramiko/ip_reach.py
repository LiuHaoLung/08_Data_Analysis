import sys
import subprocess

# 檢查 ping
def ip_reach(list):
    
    for ip in list:
        ip = ip.rstrip('\n')
        ping_reply = subprocess.call('ping %s -c 2' % ip, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
        
        if ping_reply == 0:
            print(f'{ip} is reachable.\n')
        else:
            print(f'{ip} not reachable.Check connectivity and try again.')
            sys.exit()