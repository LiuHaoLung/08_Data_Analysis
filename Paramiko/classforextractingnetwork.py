import re

a = 'Last login: Thu Sep 26 14:19:42 2019 from 10.10.10.1\r\r\nenable\r\nterminal length 0\r\nenable\r\nterminal length 0\r\nArista3>enable\r\nArista3#terminal length 0\r\nPagination disabled.\r\nArista3#\r\nconfigure terminal\r\nArista3#configure terminal\r\nArista3(config)#show interfaces loopback 0\r\nLoopback0 is up, line protocol is up (connected)\r\n  Hardware is Loopback\r\n  Internet address is 3.3.3.3/24\r\n  Broadcast address is 255.255.255.255\r\n  IP MTU 65535 bytes\r\n  Up 3 minutes, 46 seconds\r\nArista3(config)#\r\nArista3(config)#show ntp status\r\nNTP is disabled.\r\nArista3(config)#'

a.split('\r\n')
b = a.split('\r\n')
b.index('  Internet address is 3.3.3.3/24')
c = b[14]
ip = re.findall(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}",c)
print(ip)
print(ip[0])

ip = re.findall(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}",a.split('\r\n')[14])
print(ip)
print(ip[0])

ip = re.findall(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}",str(a.split('\r\n')))
print(ip)