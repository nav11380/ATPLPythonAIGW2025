def fun(f): # Passing Functions as Input
    print(f)
    f() # Nesting of Functions


def hello():
    print('hello all')

# Passing Function inside another function as input
fun(hello)