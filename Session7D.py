def square_of_number(number):
    print('1. number is: ', number, id(number)) # 10
    number = number * number
    print('2. number is: ', number, id(number)) # 100


number = 10
print('3. number is:', number, id(number)) # 10
square_of_number(number)
print('4. number is:', number, id(number)) # 10