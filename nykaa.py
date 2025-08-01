





from ATPLPythonAIGW2025.Session9C import User


def __init__ (self, name = 'NA', phone ='NA', email = 'NA',address ='NA', gender = 'NA', age = 18):
    print('constructor executed')
    print('self:', self, type(self), id(self))
    self.name = name 
    self.phone = phone
    self.email = email
    self.address = address
    self.gender = gender 
    self.age = age

def update(self, name = 'NA', phone ='NA', email = 'NA', address ='NA', gender = 'NA', age = 18):
    print('constructor executed')
    print('self:', self, type(self), id(self))
    self.name = name 
    self.phone = phone
    self.email = email
    self.address = address
    self.gender = gender 
    self.age = age

def show(self):
    print('---------------')
    print('Data for', self.name)
    print(vars(self))
    print('----------------')
    print()

john = User('John Watson', '+91 9999977777', 'john@emample.com', 'country homes', 'male', 30) 

fioana = User(name = 'fioana Flynn',
                phone  = '+91 95656 23025',
                email = fioana@example.com,
                adddress = 'country homes',
                gender = 'Female',
                age = 25)

jack = User(name= 'Jackie',email = 'jackie@example.com')

john.show()
fioana.show()
jack.show()

jack.update(name = 'jackson',
            email = 'jackson@example.com',
            adress = 'country homes')


jack.show

