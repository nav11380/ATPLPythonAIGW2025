numbers = [10, 20, 30, 40, 11]

# List Comprehension
square_numbers = [number**2 for number in numbers]
print('square_numbers:', square_numbers)

my_numbers = ['even' if number%2 == 0 else 'odd' for number in numbers]
print(my_numbers)


list1 = [1, 2, 3]
list2 = [4, 5]

result = [
    [n**2 for n in list1],
    [n**2 for n in list2],
]

print('result:', result)

# * unpacking operator
# i.e. it will append both the lists as 1 single list
# flatten the data
# from n-dimenstion you generate 1-dimenstion
result = [
    *[n**2 for n in list1],
    *[n**2 for n in list2],
]

print('result with * operator:', result)