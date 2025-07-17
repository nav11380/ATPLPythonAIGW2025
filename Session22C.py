name = 'Leo'
age = 20
email = 'leo@example.com'

user = {
    'name': 'Leo',
    'age': 20,
    'email': 'leo@example.com'
}

class User:

    def __init__(self):
        self.name = 'Leo'
        self.age = 20
        self.email = 'leo@example.com'

leo = User()

# Printing the data
print('Name:', name, 'Age:', age, 'Email:', email)

# String Formatting
print('Name: {}, Age: {} Email: {}'.format(name, age, email))

# Indexing while doing string formatting
print('Name: {0}, Age: {1} Email: {2}'.format(name, age, email))
print('Name: {1}, Age: {1} Email: {0}'.format(name, age, email))

# Key Value while doing string formatting
print('Name: {a}, Age: {b} Email: {c}'.format(a=name, b=age, c=email))

# Formatting with map i.e. using dictionaries
print('Name: {name}, Age: {age} Email: {email}'.format_map(user))
print('Name: {name}, Age: {age} Email: {email}'.format_map(vars(leo)))