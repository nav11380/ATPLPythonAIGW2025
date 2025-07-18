class User:

    def __init__(self, name=None, phone=None, email=None, address=None, age=None):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        self.age = age

        print('User Object Created...')

    def input_user_details(self):
        self.name = input('Enter Your Name: ')
        self.phone = input('Enter Your Phone: ')
        self.email = input('Enter Your Email: ')
        self.address = input('Enter Your Address: ')
        self.age = int(input('Enter Your Age: '))

    # def __str__(self): you have to return string
    def show(self):
        print('~~~~~~~~~~{} Details~~~~~~~~~~'.format(self.name))
        data = 'Phone: {phone} | Email: {email}\nAddress: {address} Age: {age}'.format_map(vars(self))
        print(data)

    def to_document(self):
        # Return Dictionary representation of the User Object :)
        return vars(self)