import logging

from kamene.all import *


logging.getLogger("kamene.runtime").setLevel(logging.ERROR) 

def qytang_ping(ip_addr):
    ping_pkt = IP(dst=ip_addr)/ICMP()
    ping_result = sr1(ping_pkt,timeout=2,verbose=False)
    if ping_result: # 有收到echo reply, 返回Packet object
        return True
    else:
        return False

