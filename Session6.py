# Loops
# Indexing
#        0   1   2   3   4
#      -5  -4   -3  -2  -1
data = [10, 20, 30, 40, 50]
print(data, type(data), id(data))

print(data[0])
print(data[-1])

print('-----------------')

# for index in range(0, 5):
for index in range(0, len(data)):
    print(data[index]) 


print('-----------------')
# Enhaced for loop or for each loop
# this works with indexed data structures in python
# as well non indexed data structures
# Without any indexing
# READ ONLY LOOP

for number in data:
    print(number)


