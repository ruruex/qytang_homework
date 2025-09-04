'''
找出连个list的相同部分，各自不同的部分
'''

# 方案二： 用函数解决
list1 = ['aaa', 111, (4, 5), 2.01]
list2 = ['bbb', 333, 111, 3.14, (4, 5)]

def find_matches(lista,listb):
    '''
    Finds and returns the mathed elements, return as list
    '''
    return [item for item in lista if item in listb]

def find_mismatches(lista,listb):
    '''
    Finds and returns the not mattached elements, return as list
    '''
    return [item for item in list1 if item not in list2]


only_in_list1 = find_mismatches(list1,list2)
for element in only_in_list1:
    print(f'{element} only in List1')

matches_in_lists = find_matches(list1,list2)
for element in matches_in_lists:
    print(f'{element} in List1 and List2')

