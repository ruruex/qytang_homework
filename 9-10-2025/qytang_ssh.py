import paramiko
import os

def qytang_ssh(ip,username,password,cmd=''):

    ssh_obj = paramiko.SSHClient()
    ssh_obj.load_host_keys(os.path.expanduser("~/.ssh/known_hosts"))
    ssh_obj.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_obj.connect(ip,port=port,username=username,password=password,timeout=2,compress=True)
    stdin,stdout,stderr = ssh_obj.exec_command(cmd)
    x = stdout.read().decode()
    return x

