'''
首先用os.popen执行linux命令ifconfig [你的网卡名], 示例输出如下
ens160: flags=4163<UP,BROADCAST,RUNNING,MULTICAST> mtu 1500
              inet 172.16.66.166 netmask 255.255.255.0 broadcast 172.16.66.255
              inet6 fe80::250:56ff:feab:59bd prefixlen 64 scopeid 0x20<link>
              ether 00:50:56:ab:59:bd txqueuelen 1000 (Ethernet)
              RX packets 174598769 bytes 1795658527217 (1.6 TiB)
              RX errors 1 dropped 24662 overruns 0 frame 0
              TX packets 51706604 bytes 41788673420 (38.9 GiB)
              TX errors 0 dropped 0 overruns 0 carrier 0 collisions 0

然后用正则表达式找到IP，掩码，广播和MAC地址
紧接着通过一种假设找到网关IP地址[你可以有你的假设](网关的前三段来至于IP地址)，并且ping网关，测试是否可达
'''
import re
import os

ifconfig_result = os.popen('ifconfig '+ ' ens160').read()
ifconfig_result = ifconfig_result.strip()
#print(ifconfig_result)

ipv4_addr = re.findall(r"inet\s(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})",ifconfig_result)[0]
#print(ipv4_addr)
netmask = re.findall(r"netmask\s(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})",ifconfig_result)[0]
#print(netmask)
broadcast = re.findall(r"broadcast\s(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})",ifconfig_result)[0]
#print(broadcast)
mac_addr = re.findall(r'ether\s((?:[0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2})',ifconfig_result)[0]
#print(mac_addr)

print(f"{('ipv4_add'):<15}: {ipv4_addr}")
print(f"{('netmask'):<15}: {netmask}")
print(f"{('broadcast'):<15}: {broadcast}")
print(f"{('mac_addr'):<15}: {mac_addr}")

# Generate ipv4 gateway address
gateway_ipv4_addr = '.'.join(ipv4_addr.split('.')[:3]) + '.254'
#print(gateway_ipv4_addr)
# pirng gateway IP addr
print('\n我们假设网关IP地址为最后一位为254, 因此网关IP地址为: ' + gateway_ipv4_addr + '\n')

# Ping test to the gateway IP
ping_result = os.popen('ping ' + gateway_ipv4_addr + ' -c 1').read()
if (re.search('Unreachable',ping_result)):
    print('网关不可达')
else:
    print('网关可达')
