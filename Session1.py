# Create Statement
# MODEL: Container -> Single Value
num1 = 10
# num1: is a reference variable created in STACK of RAM
# 10 gets strored in a Container of type int in HEAP of RAM

# Read Statement
print('num1 is:', num1)
print('type of num1 is:', type(num1))
print('num1 hashcode is:', id(num1))

# Update Statement
num1 = 20

# Read Statement -> VIEW
print('num1 now is:', num1)
print('type of num1 now is:', type(num1))
print('num1 hashcode now is:', id(num1))

# Delete Statement
# Explicit (del statement) or Implicit (Automatic)
del num1

print('num1 now is:', num1)
print('type of num1 now is:', type(num1))
print('num1 hashcode now is:', id(num1))