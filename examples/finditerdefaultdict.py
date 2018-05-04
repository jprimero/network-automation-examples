import re
from collections import defaultdict

interface_errors = """FastEthernet,1/0/1,23
FastEthernet,1/1/1,11
FastEthernet,2/1/0,42
FastEthernet,3/3/1,781
GigabitEthernet,4/0/0,89
GigabitEthernet,4/1/0,142
GigabitEthernet,3/2/0,142
GigabitEthernet,0/2/0,142
GigabitEthernet,5/1/0,46"""

int_index = defaultdict(list)
int_look_for = ('GigabitEthernet', 'FastEthernet')

for interface in int_look_for:
    for match in re.finditer(interface, interface_errors):
        int_index[interface].append(match.group())

for k,v in int_index.items():
    print(k, len(v))
