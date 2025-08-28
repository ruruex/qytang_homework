'''
字符串为ASA防火墙show conn（查看连接内容): 'TCP server 172.16.1.101:443 localserver 172.16.66.1:53710, idle 0:01:09, bytes 27575949, flags UIO'
使用正则表达式匹配，并且格式化打印后结果如下图
Protocol                : TCP
server                  : 172.16.1.101:443  
localserver             : 172.16.66.1.:53710
idle                    : 0 小时 01分钟 09秒
bytes                   : 27575949
flags                   : UIO
'''
import re

orginal_str = 'TCP server 172.16.1.101:443 localserver 172.16.66.1:53710, idle 0:01:09, bytes 27575949, flags UIO'
refine_str = orginal_str.replace(',',"   ")
re_result = re.split('\s+',refine_str)
#  print(re_result)

# refine time output
time_str = re_result[6]
h, m, s = time_str.split(':')
refine_time_str = f"{int(h)} 小时 {m.zfill(2)}分钟 {s.zfill(2)}秒" #int(h)转换为整型,去掉一个0, zfill自动补零,可选

print(f"{('Protocol'):<15}: {re_result[0]}")
print(f"{(re_result[1]):<15}: {re_result[2]}")
print(f"{(re_result[3]):<15}: {re_result[4]}")
print(f"{(re_result[5]):<15}: {refine_time_str}")
print(f"{(re_result[7]):<15}: {re_result[8]}")
print(f"{(re_result[9]):<15}: {re_result[10]}")