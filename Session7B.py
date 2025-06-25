# Function: It perform square of a number

def square(number):
    result = number*number
    return result

print('square is:', square)
# print('type of square is:', type(square))
# print('hashcode of square is:', id(square))
# print('hashcode of square is:', hex(id(square)))

# Whenever we re-define an existing function
# old function is removed from memory, and new one is constructed
def square(number1, number2):
    result = number1 * number2
    return result

print('square now is:', square)

# square(10)          # 100 # error -> as old function does not exist
result_from_square = square(10, 20)        # 200
print('result_from_square is:', result_from_square)
