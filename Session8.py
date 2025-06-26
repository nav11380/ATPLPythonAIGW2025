# Default Arguments
# You can give default values from right to left
# def add(number1=10, number2): error
# def add(number1, number2=100): ok

def add(number1=200, number2=100): 
    result = number1 + number2
    return result

# result_from_add = add(100)
# result_from_add = add()
# result_from_add = add(10, 20)
# result_from_add = add(number1=10, number2=20)
result_from_add = add(number2=10, number1=20)
print('result_from_add:', result_from_add)