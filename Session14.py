"""
Setups:
    1. Install MySQL
    2. Register online on mongodb

Query Session
    1. Reference copy operation using functions
"""

data = [1, 2, 3, 4, 5]
numbers = data # Reference Copy Operation | main frame

print('hashcode of data:', id(data))
print('hashcode of numbers:', id(numbers))

print('hashcode of data[0]:', id(data[0]))

# index: 0, 1, 2, 3, 4 as len(numbers) is 5
for index in range(len(numbers)):
    numbers[index] = numbers[index]*numbers[index]

print('hashcode of data[0]:', id(data[0]))
print('data is:', data)



def square_of_numbers(numbers):
    for index in range(len(numbers)):
        numbers[index] = numbers[index]*numbers[index]


square_of_numbers(numbers=data)  
# Reference Copy Operation 
# from main frame to square_of_numbers


