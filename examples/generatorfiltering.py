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

above100_errors = ( e for e in interface_error_details(interface_errors) 
                    if e['error'] > 100
                  )
for int_err in above100_errors:
    print(int_err)
