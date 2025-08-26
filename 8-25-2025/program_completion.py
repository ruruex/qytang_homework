department1 = "Security"
department2 = "Python"
depart1_m = "cq_bomb"
depart2_m = "qinke"
COURSE_FEES_SEC = 456789.12456
COURSE_FEES_Python = 1234.3456

# Use string formt expresssions
line1 = 'Department1 name: %-15s Manager: %-15s COURSE FEE: %-15s The End' % (department1, depart1_m, str(COURSE_FEES_SEC))

#Use new .format() method
line2 = 'Department2 name: {0:<15} Manager: {1:<15} COURSE FEE: {2:<15} The End'.format(department2, depart2_m, str(COURSE_FEES_Python))

length = len(line1)
print('='*length) # Print a line with the same length as the string
print(line1)
print(line2)
print('='*length)

