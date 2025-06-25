def square_of_numbers(numbers):
    print('[square_of_numbers] numbers is: ', numbers, id(numbers), type(numbers))
   
    for index in range(len(numbers)):
        print('[square_of_numbers]', numbers[index], type(numbers[index]), id(numbers[index]))

    for index in range(len(numbers)):
        numbers[index] = numbers[index] * numbers[index]

    print('-------------')

    print('[square_of_numbers] numbers now is: ', numbers, id(numbers), type(numbers))
    
    for index in range(len(numbers)):
        print('[square_of_numbers]', numbers[index], type(numbers[index]), id(numbers[index]))


data = [10, 20, 30, 40, 50]
print('[main] data is:', data, id(data), type(data)) 

for index in range(len(data)):
    print('[main]', data[index], type(data[index]), id(data[index]))

square_of_numbers(data)

print('---------------')
print('[main] data now is:', data, id(data), type(data)) 

for index in range(len(data)):
    print('[main]', data[index], type(data[index]), id(data[index]))
