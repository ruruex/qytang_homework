'''
字符串为MAC地址表内容: '166 54a2.74f7.0326 DYNAMIC Gi1/0/11'
使用正则表达式匹配，并且格式化打印后结果如下图:
VLAN ID         : 166
MAC             : 54a2.74f7.0326
Type            : DYNAMIC
Interface       : Gi1/0/11
'''
import re

orginal_str = '166 54a2.74f7.0326 DYNAMIC Gi1/0/11'
re_result = re.split('\s+',orginal_str)
#print(output)
print(f"{('VLAN ID'):<15}: {re_result[0]}")
print(f"{('MAC'):<15}: {re_result[1]}")
print(f"{('Type'):<15}: {re_result[2]}")
print(f"{('Interface'):<15}: {re_result[3]}")