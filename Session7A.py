# Introduction to Function
# Function has 3 components

# Create Statement: Create Function in Memory
def f(a, b):  # 1st component: name and input             
    print(a)  # 2nd component: definition (means instructions)
    print(b)
    a += b
    result = a*2
    print('result is:', result)
    # by default the last statement of any function is return
    # return means termination of function
    # return # termination of function
    return result


print('this is the first statement')

# f(10, 20)
# f(a=10, b=20) # 3rd Component: Execution of function
result_from_f = f(a=10, b=20) # 3rd Component: Execution of function
print('result_from_f is:', result_from_f)
print('this is the last statement')
