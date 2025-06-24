def max_in_list(data):
    max_number = data[0]
    for index in range(1, len(data)):
        # print('max_number:', max_number, 'data[',index,']:', data[index])
        if data[index] > max_number:
            max_number = data[index]
    
    print('-------------------------')
    print('max_number:', max_number)
    print('-------------------------')


def min_in_list(data):
    min_number = data[0]
    for index in range(1, len(data)):
        if data[index] < min_number:
            min_number = data[index]
    
    print('-------------------------')
    print('min_number:', min_number)
    print('-------------------------')


"""
numbers = [10, 17, 23, 45, 9, 12]
ipl_scores = [111, 210, 120, 97, 56, 32]
product_prices = [100, 50, 77, 80, 12, 99, 20, 200, 76, 55]

max_in_list(numbers)
max_in_list(ipl_scores)
max_in_list(product_prices)
"""