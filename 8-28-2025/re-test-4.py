'''
Get the gateway of the the Linux route -n output

'''

import os
import re

route_n_result = os.popen("route -n").read()
# print(route_n_result.split('\n'))
route_n_list =  route_n_result.split('\n')

for output in route_n_list:
    if re.search('\s+UG\s+',output):
        gateway_ip_addr = output.split()[1]

print(f'网关为:{gateway_ip_addr}')

