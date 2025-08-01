class User:
    def __init__(self, name = None, phone = None, email = None, address = None, age = None):
        self.name = name 
        self.phone = phone
        self.email = email 
        self.address = address
        self.age = age

        print("User Object Created...")

    def input_user_details(self):
        self.name = input('Enter your name')
        self.phone =input('Enter your phone')
        self.email =input('Enter your email')
        self.address =input('Enter your address')
        self.age =int(input('Enter your age'))

    def show(self):
        print('---------{} Details-----------'.format(self.name))
        data = 'Phone:{phone} | Email : {email} \ \n address = {address} |age = {age}'.format_map(vars(self))
        print(data)

    def to_document(self):
        return vars(self)

        