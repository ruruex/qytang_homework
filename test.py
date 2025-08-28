import re

txt = '''
ens160: flags=4163<UP,BROADCAST,RUNNING,MULTICAST> mtu 1500
              inet 172.16.66.166 netmask 255.255.255.0 broadcast 172.16.66.255
              inet6 fe80::250:56ff:feab:59bd prefixlen 64 scopeid 0x20<link>
              ether 00:50:56:ab:59:bd txqueuelen 1000 (Ethernet)
              RX packets 174598769 bytes 1795658527217 (1.6 TiB)
              RX errors 1 dropped 24662 overruns 0 frame 0
              TX packets 51706604 bytes 41788673420 (38.9 GiB)
              TX errors 0 dropped 0 overruns 0 carrier 0 collisions 0
'''
x = re.findall("inet\s(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", txt)
print(x)