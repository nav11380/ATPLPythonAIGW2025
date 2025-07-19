import datetime
import hashlib

# Model
class User:

    def __init__(self, name=None, phone=None, email=None, 
                 password=None, address=None, gender=None, age=None):
        self.name = name
        self.phone = phone
        self.email = email
        self.password = password
        self.address = address
        self.gender = gender
        self.age = age
        self.created_on = datetime.datetime.now()
        print('[User] Object Created')

    def input_user_details(self):
        # Logic: implement, let the user run inside a loop, till time user doesnt correct the data
        
        # Validations: Check data entered is right or wrong

        errors = []
        self.name = input('Enter Your Name: ')
        
        if len(self.name) == 0:
            errors.append('[Error] Name Cannot be Empty')

        self.phone = input('Enter Your Phone: ')
        
        if len(self.phone) != 10:
            errors.append('[Error] Phone Number Must be 10 Digits')

        self.email = input('Enter Your Email: ')

        if len(self.email) == 0:
            errors.append('[Error] Email Cannot be Empty')

        if '@' not in self.email and '.' not in self.email:
             errors.append('[Error] Email is not Correct')

        self.password = input('Enter Your Password (Min 5 Characters): ').encode('utf-8')
        self.password = hashlib.sha256(self.password).hexdigest()

        if len(self.password) < 6:
            errors.append('[Error] Password must be minimum 5 characters')

        self.address = input('Enter Your Address: ')
        if len(self.address) == 0:
            errors.append('[Error] Address Cannot be Empty')

        self.gender = input('Enter Your Gender (male/female): ')
        if self.gender != 'male' or self.gender != 'female':
            errors.append('[Error] Gender must be male or female')

        self.age = int(input('Enter Your Age: '))
        if self.age < 16:
            errors.append('[Error] Age cannot be less than 15')

        if len(errors) != 0:
            for error in errors:
                print(error)

            print('Please Correct the Above errors and Try Again')


    def show(self):
        print('~~~~~~~~~~{} Details~~~~~~~~~~'.format(self.name))
        data = 'Phone: {phone} | Email: {email} | Password {password}\nAddress: {address} | Age: {age}'.format_map(vars(self))
        print(data)

    def to_document(self):
        # Return Dictionary representation of the User Object :)
        return vars(self)