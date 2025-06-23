"""
    zomato: 20% off
          : min value of 300

    bingo: 50% off
         : min value of 500
         : max discount 150

"""

promo_code = input('Enter Promo Code: ')
amount = float(input('Enter Amount: '))

# Ladder if/else
if promo_code == 'zomato':
    if amount > 300:
        discount = 0.20 * amount
        bill_to_pay = amount - discount
        print('You got a discount of \u20b9', discount)
        print('Your amount was \u20b9', amount)
        print('Please pay: \u20b9', bill_to_pay)
    else:
        print('Please add items worth', (301-amount), 'more to get discount')
elif promo_code == 'bingo':
    if amount > 500:
        discount = 0.50 * amount
        if discount > 150:
            discount = 150
        bill_to_pay = amount - discount
        print('You got a discount of \u20b9', discount)
        print('Your amount was \u20b9', amount)
        print('Please pay: \u20b9', bill_to_pay)
    else:
        print('Please add items worth', (501-amount), 'more to get discount')
else:
    print('Invalid Coupon Code')
