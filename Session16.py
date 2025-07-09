"""
    Single Value Containers (which can hold only 1 value)
    int, float, Bool

    Multi Value Containers (which can hold lot of data)
    objects -> tuple, list, string, set, dictionary

    Sequences
        tuple
        list
        string

        storage of the data is sequential or linear

        storage of the data is non sequential or non linear
        set
        dictionary

        Properties:
        1. Indexing
        2. Negative Indexing
        3. Slicing
        4. Concatenation
        5. Multiplicity
        
        6. Membership Testing
        

"""

# 1. Indexing
# 2. Negative Indexing

# List
# 1-D List
#         -3    -2   -1
#.         0    1   2
my_data = [10, 20, 30]
print('my_data[0]: ', my_data[0])   # 10
print('my_data[-1]: ', my_data[-1]) # 30
print('length of my_data[0]: ', len(my_data)) # 3

# List of Lists
# 2-D List
numbers = [
         #.  0    1   2
            [10, 20, 30],       # 0
            [40, 50, 60],       # 1
            [70, 80, 90],       # 2
          ]

# numbers = [
#             [10, 20],
#             [40, 50, 60],
#             [70, 80, 90, 100],
#           ]

print('numbers[0]: ', numbers[0])
print('numbers[-1]: ', numbers[-1])
print('Length of numbers: ', len(numbers))
print('numbers[0][2]: ', numbers[0][2])
print('numbers[-1][-2]: ', numbers[-1][-2])

# List of List of Lists
# 3-D List
large_data = [
                [
                    #.  0    1   2
                    [10, 20, 30],       # 0
                    [40, 50, 60],       # 1     # 0
                    [70, 80, 90],       # 2
                ],
                [
                    #.  0    1   2
                    [10, 20, 30],       # 0
                    [40, 50, 60],       # 1     # 1
                    [70, 80, 90],       # 2
                ]

             ]
print('large_data[1][2][1]: ', large_data[1][2][1]) # 80
print('Length of large_data: ', len(large_data)) # 2
print('large_data[-1][-2][-2]:  ', large_data[-1][-2][-2]) # 

# name = "Johns Cafe"
# name = 'John\'s Cafe'
message = """This is Awesome
Welcome to Johns Cafe
    You get happiness with good food"""

print('message')
print(message)

print("Length of message", len(message))
print("message[1] is:", message[1])
print("message[-4] is:", message[-4])

print("message[len(message)-1] is:", message[len(message)-1])
print("message[-len(message)] is:", message[-len(message)])

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print()

# 3. Slicing
# slice -> if you want steps, explore slice as built in, in python

indexes = list(range(0, 10, 1))
negative_indexes = list(range(-1, -11, -1))
data = list(range(10, 101, 10))
print('index:', indexes)
print('index:', negative_indexes)
print('data:', data)

print(data[0 : 3]) # pickup elements starting from 0 till 2 i.e. less than 3
print(data[3 : 7]) # from 3 to 6
print(data[5 : ])  # from 5 till end
print(data[ : 4])  # 0 till 3

print('data[-5 : -2]:', data[-5 : -2]) # 60, 70, 80
print('data[ : -5]:', data[ : -5])   # 10 to 50

email = 'john@example.com'
name = email[0:4]     # john
domain = email[5:]    # example.com
print('name:', name)
print('domain:', domain)

# 4. Concatenation
# combine elements of data1 and data2 to create a new list data3
data1 = [10, 20, 30]
data2 = [40, 50, 60]

data3 = data1 + data2
print('data3:', data3)

salutation = 'Mr. '
full_name = 'John Watson'

name = salutation + full_name
print('name:', name)

# 5. Multiplicty
data4 = data1 * 3
print('data4:', data4)

# 6. Membership Testing
print('10 in data1:', 10 in data1)
print("exam in email:", 'exam' in email)
print("hello not in email:", 'hello' not in email)

# Test all 6 properties on non linear data structures as below:

# set 
data = {10, 20, 30, 40, 50} 

# dictionary
student = {
    'roll_number': 1,
    'name': 'John',
    'age': 20,
    'gender': 'male',
    'address': 'redwood shores',
}
print('20 in data:', 20 in data)
print('roll_number in student:', 'roll_number' in student)

# False: Membership Testing works only on keys in dictionary
print('1 in student:', 1 in student)
