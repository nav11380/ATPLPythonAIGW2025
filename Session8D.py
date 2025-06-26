def hello():
    print('hello all')

print('hello:', hello)

# Reference copy
bye = hello

print('bye:', bye)

bye()