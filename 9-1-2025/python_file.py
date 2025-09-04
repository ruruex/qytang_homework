import os
from pathlib import Path
import shutil

# 创建测试目录和文件
'''
import os
 
os.mkdir('test')
os.chdir('test')

qytang1 = open('qytang1','w')
qytang1.write('test file\n')
qytang1.write('this is qytang\n')
qytang1.close()

qytang2 = open('qytang2','w')
qytang2.write('test file\n')
qytang2.write('qytang python\n')
qytang2.close()

qytang3 = open('qytang3','w')
qytang3.write('test file\n')
qytang3.write('this is python\n')
qytang3.close()

os.mkdir('qytang4')
os.mkdir('qytang5')

'''

os.chdir('test')
print('文件名中包含“qytang”的文件有：')

# 遍历当前目录下的所有文件, 包括子目录
root_path = Path('.')
for file_path in root_path.glob('*'):
    if file_path.is_file():
        # 如果文件名中包含“qytang”，则打印文件名
        if 'qytang' in file_path.name:
            print(file_path)

# 文件清理
os.chdir('..')
#print(os.getcwd())
if os.getcwd() == '/root/python_basic':
    shutil.rmtree('test')