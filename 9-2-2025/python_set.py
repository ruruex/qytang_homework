'''
找出连个list的相同部分，各自不同的部分
'''

# 方案一： 不用函数解决
list1 = ['aaa', 111, (4, 5), 2.01]
list2 = ['bbb', 333, 111, 3.14, (4, 5)]
set1=set(list1)
set2=set(list2)
diff1 = set1.difference(set2)
for item in diff1:
    print(f'{item} only in List1')

diff2= set2.difference(set1)
for item in diff2:
    print(f'{item} only in List2')

insert = set1.intersection(set2)
for item in insert:
    print(item,end=' ')
print('in List1 and List2')