numbers = [10,30,50,20,40]

for outer in range(len(numbers)-1):
    for inner in range(len(numbers)-outer-1):
        if numbers[inner] > numbers[inner+1]:
            temp = numbers[inner] 
            numbers[inner] = numbers[inner+1]
            numbers[inner+1] = temp

print(numbers)