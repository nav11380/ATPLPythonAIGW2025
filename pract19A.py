"""
Doctor's App
----------
patient = patient_id,name,phone,email,address,dob,gender,created_on
 """
import datetime

class Patient:
    def __init__(self,
                patient_id = None,
                name = None,
                phone = None,
                email = None,
                address = None,
                dob = None,
                gender = None,
                created_on = None
                ):
        self.patient_id = 0
        self.name = None,
        self.phone = None,
        self.email = None,
        self.address = None,
        self.dob = None,
        self.gender = None,
        self.created_on = datetime.datetime.now()

    def input_patient_details(self):
        self.name = input("Enter your name:")
        self.phone = input("Enter your phone:")
        self.email = input("Enter your email:")
        self.address = input("Enter your address:")
        self.dob = input("Enter your dob:")
        self.gender = input("Enter your gender:")
        self.created_on = input("Enter your created_on:")

    def show(self):
        print("~~~~~~~~~~Patient~~~~~~~~~~~")
        print('Patient ID:', self.patient_id)
        print('Name:', self.name)
        print('Phone:', self.phone)
        print('Email:', self.email)
        print('Address:', self.address)
        print('DOB:', self.dob)
        print('Gender:', self.gender)
        print('Craeted On:', self.created_on)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            
        
