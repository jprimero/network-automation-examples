import re
from collections import Counter

interface_errors = """FastEthernet,1/0/1,23
FastEthernet,1/1/1,11
FastEthernet,2/1/0,42
FastEthernet,3/3/1,781
GigabitEthernet,4/0/0,89
GigabitEthernet,4/1/0,142
GigabitEthernet,3/2/0,142
GigabitEthernet,0/2/0,142
GigabitEthernet,5/1/0,46"""

def findall(text, regex):
    MATCH_RE = re.compile(regex)
    return (match.group() for match in MATCH_RE.finditer(text))

gi_list =  findall(interface_errors, r'GigabitEthernet')
fe_list =  findall(interface_errors, r'FastEthernet')

count = Counter(gi_list)
print(count)
count.update(fe_list)
print(count)
