import paramiko


def qytang_ssh(ip,username,password,port=22,cmd='ls'):

    ssh_obj = paramiko.SSHClient()
    ssh_obj.load_host_keys(r'/xxx/.ssh/known_hosts')
    ssh_obj.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_obj.connect(ip,port=port,username=username,password=password,timeout=2,compress=True)
    stdin,stdout,stderr = ssh_obj.exec_command(cmd)
    x = stdout.read().decode()
    return x

if __name__ == '__main__':
    output = qytang_ssh('10.128.1.90',username='admin',password='xxx',cmd='show ip int b \r\n')
    print(output)
    print(repr(output))