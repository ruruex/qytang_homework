import subprocess
import re
import sys

class QYTPING:

    def __init__(self,dst_ip,length=100) -> None:
        self.dst_ip = dst_ip
        self.length = int(length)
        self.result = ''
        self.srcip = None
        self.success_output = '!'
        self.failed_output = '.'

    def __str__(self) -> None:
        '''
        Define the print output
        '''
        if self.srcip:
            return f'<{self.__class__.__name__} => srcip: {self.srcip}, dstip: {self.dst_ip}, length: {self.length}>'
    
        else:
            return f'<{self.__class__.__name__} => dstip: {self.dst_ip}, length: {self.length}>'
    
    def _ping_share(self,count=1) -> None:
        '''
        Private method, shared by one() and ping()
        '''
        cmd = ['ping', self.dst_ip, '-s', str(self.length), '-c', str(count)]
        # If add srcip attribute
        if self.srcip:
            cmd.extend(['-I',self.srcip])
        try:
            self.result = subprocess.run(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                check=True,
                text=True
                )
        except subprocess.CalledProcessError as e:
           print(f"Ping failed: {e}")
           self.result = e #捕获ping命令返回非零状态码的情况（如100%丢包）, e包含stdout、stderr、returncode等属性
        except Exception as e: 
            print(f"Catched errors: {str(e)}")
            self.result = None
    
    def _parse_ping_stats(self) -> int:
        '''
        Get success and failed count
        '''
        output_list = []
        send_count = 0
        success_count = 0

        if self.result.stdout:
            output_list = self.result.stdout.split('\n')
            #print(f'output_list is {output_list}')
            for content in output_list:
                match = re.search(r'(\d+)\s+packets\s+transmitted,\s+(\d+)\s+received',content)
                if match:
                    #print(f'matched: {match.group()}')
                    send_count = int(match.group(1))
                    success_count = int(match.group(2))
                    return send_count,success_count
  
            return send_count,success_count

    def one(self) -> None:
        # ping dst_ip only once
        self._ping_share(count=1)
        send_count,success_count = self._parse_ping_stats()
        if send_count == 1 and success_count == 1: 
            print(f'{self.dst_ip} 可达！')
        else:
            print(f'{self.dst_ip} 不可达')
        
    def ping(self) -> None:
        '''
        ping 5 times
        '''
        #if self.srcip:
        #    print(f'srcip is{self.srcip}')

        self._ping_share(count=5)
        send_count,success_count = self._parse_ping_stats()
        failed_count = send_count - success_count
        if failed_count == 5:
            print (self.failed_output* failed_count)
        elif success_count ==5:
            print(self.success_output * success_count )
        else:
            print(self.success_output  * success_count + self.failed_output * failed_count)

       
class NewPing(QYTPING):
    '''
    New class inherate from the QYTPING

    '''
    def __init__(self, dst_ip, length=100) -> None:
        super().__init__(dst_ip, length)
        self.success_output = '+' 
        self.failed_output = '?'    

    def ping(self) -> None:
        '''
        Rewrite the ping method to support to change reacheable count to +, ? to not reachable
        '''
        self._ping_share(count=5)

        # 改输出已经完成，这段重复的其实也可以不写
        send_count,success_count = self._parse_ping_stats()
        failed_count = send_count - success_count
        if failed_count == 5:
            print (self.failed_output* failed_count)
        elif success_count ==5:
            print(self.success_output * success_count )
        else:
            print(self.success_output  * success_count + self.failed_output * failed_count)




if __name__ == "__main__":
    ping = QYTPING('223.5.5.5') #创建实例
    total_len = 70

    def print_new(word, s='-'):
        print('{0}{1}{2}'.format(s * int((70 - len(word))/2), word, s * int((70-len(word)/2))))
    
    print_new('print class')
    print(ping)

    print_new('ping one for sure reachable')
    ping.one() #ping一个包判断可达性

    print_new('ping five times')
    ping.ping() #模拟正常ping程序ping5个包，'!'表示通，'.'表示不通

    print_new('set payload length')
    ping.length = 200 # 设置负载长度
    print(ping) # 打印类
    ping.ping() #使用修改长度的包进行ping测试
    
    print_new('set ping src ip address')
    ping.srcip = '192.168.5.131' #修改源IP地址
    print(ping) #打印修改过的实例结果
    ping.ping() #使用修改过长度和源地址的包进行ping测试

    print_new('new class NewPing','=')
    newping = NewPing('223.5.5.5')
    newping.length = 300
    print(newping) # 打印新类的属性
    newping.ping() #NewPing类自定义过ping()这个方法，'+'表示通，'?'表示不通

#