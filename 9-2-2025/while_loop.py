'''
使用While循环监控TCP/80的HTTP服务运行状态
每一秒查看一下TCP/80(一定要区分TCP或UDP,80或8000)是否被打开，如果打开就退出循环，并且打印告警信息"HTTP (TCP/80) 服务已经被打开"
如果没开则打印"等待一秒重新开始监控!"
'''
import os
import time
import re

while True:
    
    result = os.popen('netstat -lptn ').read()
    output_list = result.split()
    
    status = False
    
    for item in output_list:
        if re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:80$',item):
            print(f'HTTP (TCP/80) 服务已经被打开')
            status = True
            break
    if status:
        break
    else:
        time.sleep(1)
        print('等待一秒重新开始监控!')
