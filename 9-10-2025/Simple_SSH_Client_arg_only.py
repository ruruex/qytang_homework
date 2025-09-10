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
import argparse, os


my_pwd=os.environ.get('Linux_pwd')

parser = argparse.ArgumentParser(description='python Simple_SSH_Client.py -i ipaddr -u username -p password -c command')
parser.add_argument('-i', '--ipaddr', type=str,required=True, help='SSH Server IP Address')
parser.add_argument('-u', '--username', type=str,default='root',  help='SSH Username')
parser.add_argument('-p', '--password', type=str,default= my_pwd,  help='SSH Password')
parser.add_argument('-c', '--command', type=str,default='', help='SSH Command')

args = parser.parse_args()





