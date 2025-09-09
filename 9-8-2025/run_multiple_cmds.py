from qytang_ssh_shell import qytang_ssh_shell

from pprint import pprint
import os


     
if __name__ == '__main__':
    my_pwd=os.environ.get('cisco_pwd')
    cmd_list = [
        'show version',
        'router ospf 1 \r\n network 192.168.5.0 0.0.0.255 area 0',
        ]
    device_list = ['10.128.1.90','admin',my_pwd]
    device_list.append(cmd_list)

    output = qytang_ssh_shell(*device_list)
    pprint(output)  