# List Data Structure in Python
print()

numbers = list(range(10, 101, 10))
print('numbers:', numbers)

numbers.append(99)
numbers.append(77)
numbers.append(111)
numbers.append(11)

print('numbers:', numbers)

print('Length of numbers:', len(numbers))
print('Sum of numbers:', sum(numbers))
print('Min of numbers:', min(numbers))
print('Max of numbers:', max(numbers))
print('Avg of numbers:', sum(numbers)/len(numbers))

data = tuple(numbers)
print('data is:', data)

# data.append(30) # error

reverse_numbers = list(reversed(numbers))
print('reverse_numbers:',reverse_numbers)

# HW: Create a function, which takes input a list and returns a list of reverse numbers
# HW: Create a function, which takes input a list and reverse numbers in the same list

idx = numbers.index(40)
print('idx is:', idx)

# num = 40
# for index in range(len(numbers)):
#     if numbers[index] == num:
#         print('number found at index:', index)
#         break

data = [10, 30, 50, 20, 5, 30, 15]
names = ['john', 'abel', 'sia', 'kim', 'anna', 'joe']

data.sort()
names.sort()
print('data:', data)
print('names:', names)

print()

names.remove('abel')
data.remove(30)
data.remove(15)

print('data:', data)
print('names:', names)

data = [10, 20, 30, 40, 50]
print('data:', data)
data.pop()
data.pop(0)

print('data after pop:', data)

data.clear()
print('data after clear:', data)

data = [10, 20, 30, 40, 50]
print('data is:', data)
data.append(99)
data.insert(2, 77)
data.insert(-1, 88)
print('data now is:', data)


# del data[1]
# del data

