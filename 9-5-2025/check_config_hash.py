from qytang_ssh import qytang_ssh

import re
import hashlib
import time
import os

def qytang_getconfig(ip,username='admin',password='') -> str: 
    '''
    Get the configuration from the network device
    '''
    try:
        running_config = qytang_ssh(ip,username=username,password=password,cmd='show running-config')
        running_config_section = re.search(r'(\shostname[\s\S]*?^end)',running_config,re.MULTILINE)
        #print(running_config_section.group(1))
        #print(repr(running_config.group(1))) # troubleshooting the original output including end of 
        if running_config_section: # if matches
            return running_config_section.group(1)
        else:
            return None
    except Exception:
        return None

def get_config_hash(running_config) -> str:
    '''
    Get the intput string's hex md5 output
    '''
    if running_config:
        hash_obj = hashlib.md5()
        hash_obj.update(running_config.encode())
        return hash_obj.hexdigest()
    else:
        return None


def qytang_check_diff(ip,username,password):
    '''
    Compare the configruation
    '''
    before_md5=''  # 上一次的md5值

    while True:
        time.sleep(5)
        latest_config = qytang_getconfig(ip,username,password)

        if latest_config:
            # 计算当前的md5值
            current_md5 = get_config_hash(latest_config)
            print(current_md5)

            # 检查是否与上次相同
            if before_md5 !='' and current_md5 != before_md5:
                print('MD5 value changed')
                break
            
            # 更新上一次的md5值
            before_md5 = current_md5

        else: # retry in 5s
            continue


     
if __name__ == '__main__':
    my_pwd=os.environ.get('cisco_pwd')
    device = ['10.128.1.90','admin',my_pwd]
    qytang_check_diff(*device)