"""
Recursion - Memory Stack

    1. function
    2. data
    3. requirement: iteration (similar to loops)

    
    loop -> 0 ...... n (loop terminate)
         -> linear approach

    non linear - trees and graphs
    in function, we can put up logic where to go
    recursion is typically to be used for non linear approach

    Loops Vs Recursion ? 

"""

# factorial: 5! -> 5 * 4 * 3 * 2 * 1 * (0!) -> 1
# 5! = 120

"""
def factorial(number):
    
    result = 1
    # while number >=1:
    #     result = result * number
    #     number -= 1

    for data in range(number, 1, -1):
        result = result * data

    return result
"""

def factorial(number):
    if number == 0:
        return 1
    else:
        result = number * factorial(number=number-1)
        return result

# in the main, we have 2 variables: data and result
data = 5
result = factorial(number=data)
print('result:', result)

"""
    fibonacci series with recursion
    0 1 1 2 3 5 8 13 ......

    number1 = 0
    number2 = 1

    number3 = number1 + number2
    number4 = number3 + number2
    ...
    .......
    ..........

"""