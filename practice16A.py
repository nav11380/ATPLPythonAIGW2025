numbers = list(range(10,101,10))
print("numbers:", numbers)

numbers.append(99)
numbers.append(77)
numbers.append(111)
numbers.append(11)

print("numbers:", numbers)
print('lenghth of numbers:', len(numbers))
print('sum of numbers:', sum(numbers))
print('min of numbers:', min(numbers))
print('max of numbers:', max(numbers))
print('avg of numbers:', sum(numbers)/ len(numbers))

data = tuple(numbers)
print('data is :',data)

reverse_numbers = list(reversed(numbers))
print('reverse_numbers',reverse_numbers)
print()

idx = numbers.index
print('idx is:', idx)
print()
num = 40
for index in range(len(numbers)):
    if numbers[index] == num:
        print("number found at index:, index" )
        break

data = [10,20,30,40,50]
print('data',data)
