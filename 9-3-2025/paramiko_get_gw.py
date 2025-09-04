import paramiko
import os
import re

my_pwd=os.environ.get('Linux_pwd')


def qytang_ssh(ip,username,password,port=22,cmd='ls'):

    ssh_obj = paramiko.SSHClient()
    ssh_obj.load_host_keys(r'C:\Users\xxx\.ssh\known_hosts')
    ssh_obj.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_obj.connect(ip,port=port,username=username,password=password,timeout=5,compress=True)
    stdin,stdout,stderr = ssh_obj.exec_command(cmd)
    x = stdout.read().decode()
    return x

def get_gw(result):
    
    route_n_list =  result.split('\n')

    for output in route_n_list:
        if re.search('\s+UG\s+',output):
            gateway_ip_addr = output.split()[1]

    return gateway_ip_addr

def ssh_get_route(ip,username,password):
    ssh_get_route_output = qytang_ssh(ip,username,password,cmd='route -n')
    return get_gw(ssh_get_route_output)


if __name__ == '__main__':
    print(qytang_ssh('10.128.1.68','root',my_pwd))
    print(qytang_ssh('10.128.1.68','root',my_pwd,cmd='pwd'))
    print('网关为:')
    print(ssh_get_route('10.128.1.68','root',my_pwd))