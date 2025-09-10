'''
create a argparse.ArgumentParser object with
usage: python Simple_SSH_Client.py -i ipaddr -u username -p password -c command

Optional arguments:
-h,--help       show this help message and exit
-i IPADDR,--ipaddr IPADDR SSH Server
-u USERNAME,--username USERNAME SSH Username
-p PASSWORD,--password PASSWORD SSH Password
-c COMMAND,--command COMMAND SSH Command

'''
import argparse, os, sys
import paramiko

from qytang_ssh import qytang_ssh

my_pwd=os.environ.get('Linux_pwd')

parser = argparse.ArgumentParser(description='python Simple_SSH_Client.py -i ipaddr -u username -p password -c command')
parser.add_argument('-i', '--ipaddr', type=str,  help='SSH Server IP Address')
parser.add_argument('-u', '--username', type=str,default='root',  help='SSH Username')
parser.add_argument('-p', '--password', type=str,default=my_pwd , help='SSH Password')
parser.add_argument('-c', '--command', type=str,default='ls -l', help='SSH Command')

args = parser.parse_args()

if args.ipaddr is None:
    print("Please see usage with -h")
    sys.exit()
else:
    device_parameter_list =[args.ipaddr,args.username,args.password,args.command]
    result=qytang_ssh(*device_parameter_list)
    if result is not None:
        print(result)

