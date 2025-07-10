my_data = {
    101: 'John',
    201: 'Jennie',
    501: 'Sia',
    99: 'Joe',
    25: 'Kim',
    201: 'Anna',
    21: 'Joe',
}

keys = list(my_data.keys())
values = list(my_data.values())
items = list(my_data.items())

print('keys:', keys)
print('values:', values)
print('items:', items)

# Enhanced For Loop
print('Printing Keys...')
for key in my_data.keys():
    print(key)

print('Printing Values...')
# Enhanced For Loop
for value in my_data.values():
    print(value)

print('Printing Items...')
for item in my_data.items():
    print(item)
    print(item[0], item[1])
    print('``````````````````````')