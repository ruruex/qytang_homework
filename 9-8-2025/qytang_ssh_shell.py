import paramiko
import time
import os

def qytang_ssh_shell(ip,username,password,cmd_list=[],enable_pass='',wait_time=2,verbose=True):
    '''
    SSH to the ip, execute the comamnds in the cmd_list, apply enable if needed, return result if verbose=True
    '''
    output_result_dict = {}

    ssh_obj = paramiko.SSHClient()
    ssh_obj.load_host_keys(os.path.expanduser("~/.ssh/known_hosts"))
    ssh_obj.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # Create shell for sending multiple commands
        ssh_obj.connect(ip,port=22,username=username,password=password,timeout=2,compress=True)
        ssh_shell = ssh_obj.invoke_shell() 
        
        # wait for ssh login to complete
        time.sleep(wait_time)
        ssh_shell.recv(65535).decode() 

        # Disable paging
        ssh_shell.send('terminal length 0\n')
        time.sleep(wait_time)
        ssh_shell.recv(65535)

        # Check for enable mode
        if enable_pass != '':
            ssh_shell.send('enable\n')
            time.sleep(wait_time)
            ssh_shell.recv(65535).decode() 
            ssh_shell.send(enable_pass+'\n') # the enable password
            time.sleep(wait_time)
            ssh_shell.recv(65535).decode() 
            print('enter enable mode')
        else:
            print('Already in enable mode')


        # execute the commands in the list
        for cmd in cmd_list:

    
            print(f'To run command: {cmd}')
            # for config mode command, we need to go to the mode
            if 'router ospf' in cmd: 
                ssh_shell.send('configure terminal\n')
                time.sleep(wait_time)
                ssh_shell.recv(65535).decode()
            
            # Run the actual configure command
            cmd = cmd.strip()
            ssh_shell.send(cmd+'\n')
            time.sleep(wait_time)

            result =''
            while True:
                if ssh_shell.recv_ready():
                    result += ssh_shell.recv(65535).decode()
                    # stop once we see the router prompt 
                    if result.strip().endswith('#'):
                        break
            
            output_result_dict[cmd] = result
                
        # close the ssh session
        ssh_shell.send('end\n')           
        time.sleep(1)
        ssh_obj.close()
        
    except Exception as error_msg:
        print(f'Error msg: {error_msg}')
        return None
    
    if verbose:
        return output_result_dict

