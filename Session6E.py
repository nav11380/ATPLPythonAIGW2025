"""
    f(x) = 2x + 1
    x: 1
    f(1) = 3
    f(2) = 5

    f(a,b) = a*a + b*b + 2*a*b
    f(2,2) = 4 + 4 + 8
    f(2,2) = 16

"""

def f(x):
    result = 2*x + 1
    print('result:', result)

def fun(a,b):
    result = a*a + b*b + 2*a*b
    print('result:', result)

f(1)
f(2)
f(-5)
fun(2,2)
fun(4,5)