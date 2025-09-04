import logging

from kamene.all import *

'''
Test scrip from interactive cmd:
logging.getLogger("kamene.runtime").setLevel(logging.ERROR) # 关闭不必要的报错
ping_pkt = IP(dst='223.5.5.5')/ICMP()
ping_result = sr1(ping_pkt, timeout=2, verbose=True) # Ping并且把返回结果复制给ping_result
ping_result.show() # 查看回显结果
'''

logging.getLogger("kamene.runtime").setLevel(logging.ERROR) 

def qytang_ping(ip_addr):
    ping_pkt = IP(dst=ip_addr)/ICMP()
    ping_result = sr1(ping_pkt,timeout=2,verbose=False)
    if ping_result: # 有收到echo reply, 返回Packet object
        print(f'从 {ping_result.dst} 到 {ping_result.src} 通！')
    else:
        print(f'从 {ping_pkt.src} 到 {ping_pkt.dst} 不通！')

qytang_ping('223.5.5.5')
qytang_ping('10.10.10.1')