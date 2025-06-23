num1 = 8
num2 = 2
result1 = num1 >> num2 # divide by 2 pow num2
result2 = num1 << num2 # multiply by 2 pow num2
print("result1:", result1)
print("result2:", result2)

data = 8
key = 2
encrypted_data = data >> key
print('encrypted_data', encrypted_data)
original_data = encrypted_data << key
print('original_data', original_data)