'''
把五天前的日期和时间，存入一个用当前日期和时间命名的文件中
'''

from datetime import datetime, timedelta
import os

# 获取当前日期和时间
now = datetime.now()

# 计算五天前的日期和时间
five_days_ago = now - timedelta(days=5)

# 格式化日期和时间为字符串
now_str = now.strftime('%Y-%m-%d_%H-%M-%S')
five_days_ago_str = five_days_ago.strftime('%Y-%m-%d %H:%M:%S.%f')

# 创建文件并在当前目录写入内容
current_dir = os.path.dirname(os.path.abspath(__file__))
file_name = f"save_fivedayago_time_{now_str}.txt"
file_path = os.path.join(current_dir, file_name)


with open(file_path, 'w') as f:
    f.write(f"{five_days_ago_str}")