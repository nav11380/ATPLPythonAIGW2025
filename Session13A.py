# Sort Function
def sort(data, low_to_high=0):
    
    if low_to_high == 0:
        for outer in range(len(data)-1):
            for inner in range(len(data)-outer-1):
                if data[inner] > data[inner+1]:
                    temp = data[inner]
                    data[inner] = data[inner+1]
                    data[inner+1] = temp

    else:
        for outer in range(len(data)-1):
            for inner in range(len(data)-outer-1):
                if data[inner] < data[inner+1]:
                    temp = data[inner]
                    data[inner] = data[inner+1]
                    data[inner+1] = temp


numbers = [10, 30, 70, 50, 40, 20, 80]
print('numbers: ')
print(numbers)

# sort(data=numbers)
sort(data=numbers, low_to_high=1)

print('sorted numbers: ')
print(numbers)

names = ['john', 'sia', 'kim', 'anna', 'ben']
print('names: ')
print(names)

sort(data=names)
print('sorted names: ')
print(names)


