'''
port_list = ['eth 1/101/1/42','eth 1/101/1/26','eth 1/101/1/23','eth 1/101/1/7','eth 1/101/2/46','eth 1/101/1/34','eth 1/101/1/18','eth 1/101/1/13','eth 1/101/1/32','eth 1/101/1/25','eth 1/101/1/45','eth 1/101/2/8']

需要排序的结果:
['eth 1/101/1/7', 'eth 1/101/1/13', 'eth 1/101/1/18', 'eth 1/101/1/23', 'eth 1/101/1/25', 'eth 1/101/1/26', 'eth 1/101/1/32', 'eth 1/101/1/34', 'eth 1/101/1/42', 'eth 1/101/1/45', 'eth 1/101/2/8’,'eth 1/101/2/46’]
'''
# lamda 方法实现
port_list = ['eth 1/101/1/42','eth 1/101/1/26','eth 1/101/1/23','eth 1/101/1/7','eth 1/101/2/46','eth 1/101/1/34','eth 1/101/1/18','eth 1/101/1/13','eth 1/101/1/32','eth 1/101/1/25','eth 1/101/1/45','eth 1/101/2/8']

sorted_port_list = sorted(port_list, key=lambda x: [int(num) for num in x.split()[1].split('/')])
port_list = []
for port in sorted_port_list:
    port_list.append(port)

print(port_list)

'''
# 使用一般方法实现，思路一致

port_list2 = ['eth 1/101/1/42','eth 1/101/1/26','eth 1/101/1/23','eth 1/101/1/7','eth 1/101/2/46','eth 1/101/1/34','eth 1/101/1/18','eth 1/101/1/13','eth 1/101/1/32','eth 1/101/1/25','eth 1/101/1/45','eth 1/101/2/8']

def sort_the_int_number(interface):
    # 分割出输入的interface中的number,例如1/101/1/26
    num_part = interface.split()[1]
    # 按"/"分割出数字，并转换成整数列表, 行如: [1, 101, 1, 42],[1, 101, 1, 26]
    return_list = [int(num) for num in num_part.split('/')]
    print(f'retur_list is {return_list}')
    return return_list

sorted_port_list = sorted(port_list2, key=sort_the_int_number)

# 打印排序结果
print(f'sorted_port_list is {sorted_port_list}')
for port in sorted_port_list:
    print(port)
'''