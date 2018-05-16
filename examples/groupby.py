from operator import itemgetter
from itertools import groupby

interface_errors = """FastEthernet,1/0/1,23
FastEthernet,1/1/1,11
FastEthernet,2/1/0,42
FastEthernet,3/3/1,781
GigabitEthernet,4/0/0,89
GigabitEthernet,4/1/0,142
GigabitEthernet,3/2/0,142
GigabitEthernet,0/2/0,142
GigabitEthernet,5/1/0,46"""

def interface_error_details(text):
    for line in text.splitlines():
        name, number, error = line.split(',')
        yield {"name": name, "number": number, "error": int(error)}

int_err = interface_error_details(interface_errors)
int_err_sorted = sorted(int_err, key=itemgetter('name'))

print('using groupby:')
for name, interfaces in groupby(int_err_sorted, key=itemgetter('name')):
    print(name)
    for i in interfaces:
        print('    ', i)

# alternative approach using simple defaultdict
from collections import defaultdict

interface_errors_by_name = defaultdict(list)

for row in interface_error_details(interface_errors):
    interface_errors_by_name[row['name']].append(row)

print('using defaultdict:')
for k,v in interface_errors_by_name.items():
    print(k)
    for i in v:
        print('    ',i)
