interface_errors = """FastEthernet,1/0/1,23
FastEthernet,1/1/1,11
FastEthernet,2/1/0,42
FastEthernet,3/3/1,781
GigabitEthernet,4/0/0,89
GigabitEthernet,4/1/0,142
GigabitEthernet,3/2/0,142
GigabitEthernet,0/2/0,142
GigabitEthernet,5/1/0,46"""

from collections import namedtuple

Interface = namedtuple('Interface', ['name', 'number', 'error'])
int_details = [ Interface(*i.split(',')) for i in interface_errors.splitlines() ]
int_details.sort(key=lambda i: (int(i.error), i.name) )

for x in int_details:
    print(x)

# namedtuples are immutable but we can use _replace to change some value

print(list(filter(lambda s: s.number == '1/1/1', int_details)))
one = None

# find the entry with number='1/1/1'
for i,v in enumerate(int_details):
    if v.number == '1/1/1':
        one = i

# replace it's error value
print(int_details[one])
int_details[one] = int_details[one]._replace(error='20')
print(int_details[one])
