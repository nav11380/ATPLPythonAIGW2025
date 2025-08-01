import datetime
class User:

    def __init__(self, name="", phone="", email="", password = "" ,address="", gender= "", age=0):
        self.name = name
        self.phone = phone
        self.email = email
        self.password = password
        self.address = address
        self.gender = gender
        self.age = age
        self.created_on = datetime.datetime.now()
        print('[User] Object created')

   
    # def __str__(self): you have to return string
    def show(self):
        print('~~~~~~~~~~{} Details~~~~~~~~~~'.format(self.name))
        data = 'Phone: {phone} | Email: {email}\nAddress: {address} Age: {age}'.format_map(vars(self))
        print(data)

    def to_document(self):
        # Return Dictionary representation of the User Object :)
        return vars(self)
