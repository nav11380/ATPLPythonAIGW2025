name = 'leo'
age = 20
email = 'leo@example.com'

user = {
    'name' :'leo',
    'age' : 20,
    'email' : 'leo@example.com'

}

class User:
    def __init__(self):
        self.name = 'leo'
        self.age = 20
        self.email = 'leo@example.com'

print('Name:',name,'Age',age,'Email',email )

print('Name:'{} 'Age'{},'Email'{}'.format(name,age,email