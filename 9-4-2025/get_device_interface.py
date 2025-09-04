from qytang_ping import qytang_ping
from qytang_ssh import qytang_ssh

import re
import pprint
import os

def qytang_get_if(*ips,username,password):
    
    device_dict = {}  # 存储所有设备输出的最终字典

    for ip in ips:
        
        if(qytang_ping(ip)):

            # 每次处理新IP时，创建新的接口字典
            device_if_dict = {}

            output = qytang_ssh(ip,username,password,cmd='show ip interface brief') #连接到设备取得output
           
            pattern = re.compile(r'^(\w+[\/-]?\d+)\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})') #查找及匹配interface和IPv4地址,[\/-]?考虑到真实环境中的Gi1/0/1/1问题
            for item in output.split('\n'): # 按行分割为list，遍历
                match = pattern.search(item)
                if match: # 如果有匹配
                    interface = match.group(1) # interface name
                    ip_addr = match.group(2) # ipv4 addr
                    device_if_dict[interface] = ip_addr
            
            device_dict[ip] = device_if_dict # 完成interface抓取、处理循环后，存于以ip为key的字典
            #print(f'device_dict is {device_dict}')
        else:
            device_dict[ip] = {}
            continue # pass the device not ping responsive

    return device_dict


if __name__ == "__main__":
    my_pwd=os.environ.get('cisco_pwd')
    pprint.pprint(qytang_get_if('10.128.1.90','10.128.1.92','10.128.1.91',username='admin',password=my_pwd),indent=4)