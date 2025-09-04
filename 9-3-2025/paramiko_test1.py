# Need to run on windows client, connect to the Rocky Linux test env

import paramiko

import os

def qytang_ssh(ip,username,password,port=22,cmd='ls'):

    ssh_obj = paramiko.SSHClient()
    ssh_obj.load_host_keys(r'C:\Users\xxx\.ssh\known_hosts')
    ssh_obj.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_obj.connect(ip,port=port,username=username,password=password,timeout=5,compress=True)
    stdin,stdout,stderr = ssh_obj.exec_command(cmd)
    x = stdout.read().decode()
    return x

my_pwd=os.environ.get('Linux_pwd')

if __name__ == '__main__':
    print(qytang_ssh('10.128.1.68','root',my_pwd))
    print(qytang_ssh('10.128.1.68','root',my_pwd,cmd='pwd'))