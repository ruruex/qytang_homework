'''
Clone L1 list, sort it, but not impact the l1 original order
'''
l1 = [4,5,7,1,3,9,0]
l2 = l1.copy()
l2.sort()
#print(l2)
for i in range(len(l1)):
    print(f"{l1[i]} {l2[i]}")