numbers = [10, 17, 23, 45, 9, 12]
ipl_scores = [111, 210, 120, 97, 56, 32]
product_prices = [100, 50, 77, 80, 12, 99, 20, 200, 76, 55]

max_number = numbers[0]
for index in range(1, len(numbers)):
    print('max_number:', max_number, 'numbers[',index,']:', numbers[index])
    if numbers[index] > max_number:
        max_number = numbers[index]

print('numbers | max_number:', max_number)
print()

max_number = ipl_scores[0]
for index in range(1, len(ipl_scores)):
    print('max_number:', max_number, 'ipl_scores[',index,']:', ipl_scores[index])
    if ipl_scores[index] > max_number:
        max_number = ipl_scores[index]

print('ipl_scores | max_number:', max_number)
print()

max_number = product_prices[0]
for index in range(1, len(product_prices)):
    print('max_number:', max_number, 'product_prices[',index,']:', product_prices[index])
    if product_prices[index] > max_number:
        max_number = product_prices[index]

print('ipl_scores | max_number:', max_number)