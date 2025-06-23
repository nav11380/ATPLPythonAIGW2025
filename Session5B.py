coupon_code = input('Enter Coupon Code: ')
billing_amount = int(input('Enter Billing Amount:'))

"""
# Simple or Regular if/else
if billing_amount > 449:
    print('coupon can be applied')
    print('thank you')
else:
    print('coupon cannot be applied')
    print('amount is low')
"""

"""
# Nested if/else (Filteration)
if coupon_code == 'NOMNOW150':
    print('coupon can be applied')
    if billing_amount > 449:
        billing_amount -= 150 # billing_amount = billing_amount - 150
        print('please pay:', billing_amount)
        print('thank you')
    else:
        print('sorry, applied coupon is not available')
        print('add items worth', (450-billing_amount),'more')
else:
    print('coupon invalid. Please check and apply again')
"""

if coupon_code == 'NOMNOW150' and billing_amount > 449:
    print('coupon can be applied')
    billing_amount -= 150 # billing_amount = billing_amount - 150
    print('please pay:', billing_amount)
    print('thank you')
else:
    print('either coupon or billing amount is failing')

