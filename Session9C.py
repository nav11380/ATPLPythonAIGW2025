class User:
    
    # Constructor: is meant ot create
    # 1: Object Contsruction
    # 2: To Standardize the Object
    #    Add attributes as input to constructor after self    
    def __init__(self, name='NA', phone='NA', email='NA', address='NA', gender='NA', age=18):
        print('constructor executed')
        print('self:', self, type(self), id(self))
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        self.gender = gender
        self.age = age

    def update(self, name='NA', phone='NA', email='NA', address='NA', gender='NA', age=18):
        print('constructor executed')
        print('self:', self, type(self), id(self))
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        self.gender = gender
        self.age = age

    # Read Operation
    def show(self):
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('Data for', self.name)
        print(vars(self))
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print()




john = User('John Watson', '+91 99999 11111', 'john@example.com', 
            'Country Homes', 'male', 30)

fionna = User(name='Fionna Flynn', 
              phone='+91 99999 22222', 
              email='fionna@example.com',
              address='redwood shores', 
              gender='female', 
              age=28)

jack = User(name='Jackie', email='jackie@example.com')

# print('data for john')
# print(vars(john))


# print('data for fionna')
# print(vars(fionna))

# print('data for jack')
# print(vars(jack))

john.show()
fionna.show()
jack.show()

jack.update(name='Jackson', 
            email='jackson@example.com', 
            address='country homes')

jack.show()

# Delete is manual, and in python we do not do deletions for Objects
# Python has a Garabage Collector Program
# which automatically detectes ununsed objects and remove them from memory
# As a developer, i am free from cleaning memory

# Manual: Rather not required
# del john