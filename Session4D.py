# Controller: Operators
# Arithmetic Operators: +, -, *, /, **, //, %

cab_fare = 1000
taxes = 0.18
tax_to_pay = cab_fare * taxes

amount_to_pay = cab_fare + tax_to_pay

print('tax_to_pay is:', tax_to_pay)
print('amount_to_pay is:', amount_to_pay)

number1 = 10
number2 = 3
# result = number1 / number2 # floating point division
result = number1 // number2  # integral division
print('result:', result)

number3 = 2
number4 = 4
number5 = number3 ** number4
print('number5:', number5)

# Number System -> Explore it, if you do not know it
print(number1)
print(bin(number1))
print(oct(number1))
print(hex(number1))