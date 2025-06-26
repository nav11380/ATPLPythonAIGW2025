"""
def add(n1, n2, n3):
    result = n1 + n2 + n3
    print('result:', result)
"""

# *args: multiple arguments or variable arguments
# In python, if you redefine a function, 
# it overwrites old definition
# i.e. it will create a new function
# * args -> receiving input as tuple
def add(*args):
    print(args)
    print(sum(args))
    # print(type(args))
    # print(id(args))

add(10, 20, 30)
add(10, 20, 30, 40, 50)
add(10, 20, 30, 40, 50, 60, 70, 80)

def multiply(**kwargs):
    print(kwargs)
    print(type(kwargs))
    print(id(kwargs))

    # Logic to multiply all numbers:
    # You can explore
    # we will do it after sometime


multiply(a=10, b=20, c=30)

def register_user(**user):
    print(user)
    # save data in database: future action


register_user(name='Ishant', email='ishant@auribises.com', gender='male')


def fun(*args, **kwargs):
    print(args)
    print(kwargs)

fun(10, 20, 30, name='john', age=20, email='john@example.com')


