"""my_list = list()
print('my_list',my_list,type(my_list))

my_dictionary ={}
print('my_dictionary',my_dictionary,type(my_dictionary))"""

my_data = {
    101 : 'John',
    201 : 'Jennie',
    501 : 'sia',
    25 : 'kim',
    201 : 'anna',

}
print('my_data')
print(my_data)

print('len(my_data)',len(my_data))
print('max(my_data)',max(my_data))
print('min(my_data)',min(my_data))
print('sum(my_data',sum(my_data))

my_data = {
    'jo' : 'John',
    'je' : 'Jennie',
    'si' : 'sia',
    'ki' : 'kim',
    'an' : 'anna',

}
print('my_data')
print(my_data)
print('len(my_data)',len(my_data))
print('max(my_data)',max(my_data))
print('min(my_data)',min(my_data))

value = my_data.get(101)
print('value',value)
 
my_data[101] ='joseph'
print(my_data)

my_data.pop(25)
print('my data after the pop')
print(my_data)

my_data[444] = 'anna'
print(my_data)