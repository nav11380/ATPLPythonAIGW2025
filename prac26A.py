#patient object :name , phone, email ,address ,gender , age , weight, bp ,sugar,temperature, allergies
import datetime
class Patient:
   
    def __init__(self, name='', phone='', email='', address='', 
                 gender='', age=0, doctor_id=''):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        self.gender = gender
        self.age = age
        self.doctor_id = doctor_id
        self.created_on = datetime.datetime.now

    def to_document(self):
        return vars(self)

    def show(self):
        pass