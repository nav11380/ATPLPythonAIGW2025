# Explore Dictionary Data Structure

# In Dictionary keys are either number(int) or text(string)
# value can be any data

# Dictionary -> Keys cannot be duplicated. They are unique
#            -> But value can be duplicated

my_data = {
    101: 'John',
    201: 'Jennie',
    501: 'Sia',
    99: 'Joe',
    25: 'Kim',
    201: 'Anna',
    21: 'Joe',
}

"""
my_data = {
    'jo': 'John',
    'je': 'Jennie',
    'si': 'Sia',
    'jj': 'Joe',
    'ki': 'Kim',
}
"""

print('my_data')
print(my_data)

# Utility functions -> they work on keys
print('len(my_data):', len(my_data))
print('min(my_data):', min(my_data))
print('max(my_data):', max(my_data))
print('sum(my_data):', sum(my_data))

# Reading data from Dictionary | Single Element
# value = my_data[101]
value = my_data.get(101)
print('value:', value)

# Update
my_data[101] = 'Joseph'
print(my_data)

# Delete
my_data.pop(25)
# del my_data[25]
print('my_data after pop(25)')
print(my_data)

# add a new element
my_data[444] = 'Anna'
print(my_data)