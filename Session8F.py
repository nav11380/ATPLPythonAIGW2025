def fun():
    print('this is a function')

# print('fun:', fun)

def hello():
    return fun

result = hello()
print('result:', result)

result()