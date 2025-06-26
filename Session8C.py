"""
numbers = [10, 20, 30]
max_number = numbers[0]
for index in range(1, len(numbers)):
    if max_number < numbers[index]:
        max_number = numbers[index]

print('max_number:', max_number)
"""
# Problem Statement: Find Maximum from a List of Numbers
# Smallest Problem: numbers = [10]
# Next Problem: numbers = [10, 20] -> if numbers[0] > numbers[1]
#                                        return numbers[0]
#                                     else
#                                        return numbers[1]

def get_max(data, length):
    
    # Base Case
    if length == 1:
        return data[0]
    else:
        previous = get_max(data, length-1) # recursion
        current = data[length-1]

        if previous > current:
            return previous
        else:
            return current

numbers = [10, 20, 30]
max_in_numbers = get_max(data=numbers, length=len(numbers))
print('max_in_numbers:', max_in_numbers)

# Write program to fetch min in mumbers list
# draw stack heap for 5 numbers

