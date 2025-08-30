'''
把防火墙状态信息表存为字典!

注意:一定要考虑很多很多行的可能性

asa_conn = "TCP Student 192.168.189.167:32806 Teacher 137.78.5.128:65247, idle 0:00:00, bytes 74, flags UIO\n TCP Student 192.168.189.167:80 Teacher 137.78.5.128:65233, idle 0:00:03, bytes 334516, flags UIO"

'''
import re

asa_conn = 'TCP Student 192.168.189.167:32806 Teacher 137.78.5.128:65247, idle 0:00:00, bytes 74, flags UIO\n \
    TCP Student 192.168.189.167:80 Teacher 137.78.5.128:65233, idle 0:00:03, bytes 334516, flags UIO'

asa_dict = {}

for message in asa_conn.split('\n'):
    #print(message)
    ip_port_pattern = re.compile(r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5})")
    ip_port_list = re.findall(ip_port_pattern,message)

    bytes_flags_pattern = re.compile(r"bytes\s(\d+),\s+flags\s+(\w+)")
    bytes_flags_list = re.findall(bytes_flags_pattern,message)

    ip_port_tuple = ip_port_list[0] + ip_port_list[1]
    bytes_flags_tuple = bytes_flags_list[0]

    asa_dict[ip_port_tuple] = bytes_flags_tuple

print('打印分析后的字典！')
print(asa_dict)


print('\n格式化打印输出\n')
for key,value in asa_dict.items():
    src_ip,src_ip_port,dst_ip,dst_ip_port = key
    bytes_value,flags = value
    format_str1 = (f"{'src_ip':^14}:{src_ip:^18}|"
                    f"{'src_ip_port':^14}:{src_ip_port:^18}|"
                    f"{'dst_ip':^14}:{dst_ip:^18}|"
                    f"{'dst_ip_port':^14}:{dst_ip_port:^18}")
    format_str2 = (f"{'bytes':^14}:{bytes_value:^18}|"
                    f"{'flags':^14}:{flags:^18}")
    print(format_str1)
    print(format_str2)
    print("="* ((14+18)*4 + 4))




#print(f"{('接口'):<8}: {formatted_str[0]}")
    