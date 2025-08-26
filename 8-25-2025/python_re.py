import re

str1 ='Port-channel1.189    192.168.189.254     YES     CONFIG    up'
formatted_str =re.split('\s+',str1)

print(f"{('接口'):<8}: {formatted_str[0]}")
print(f"{('IP地址'):<8}: {formatted_str[1]}")
print(f"{('状态'):<8}: {formatted_str[2]}")