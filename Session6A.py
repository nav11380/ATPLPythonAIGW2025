# for row in range(0, 5, 1): # 0, 1, 2, 3, 4
for row in range(0, 5, 2): # 0, 2, 4
    print('row', row)

print('-------------')

for row in range(5, 0, -1):
    print('row', row)

print('-------------')

# Use range function to auto generate some numbers as a list
numbers = list(range(5, 0, -1))
print(numbers)

