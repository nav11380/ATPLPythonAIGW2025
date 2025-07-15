"""
    Doctor's App
    ------------
    
    # 1. Think of an Object
    Patient: patient_id, name, phone, email, address, dob, gender, created_on

    ORM Fundamental

    create table Patient(
        patient_id int primary key auto_increment,
        name varchar(256),
        phone varchar(20),
        email varchar(256),
        address text,
        dob date,
        gender varchar(20),
        created_on datetime
    );

    insert into Patient values(null, 'fionna', '9876512345', 'fionna@example.com','redwood shores', '2000-04-10', 'female', '2025-07-15 11:16:00')

"""

# Model or Object or Entity or Bean

import datetime

# 2. Write its class
class Patient:

    def __init__(self, 
                 name=None, 
                 phone=None, 
                 email=None, 
                 address=None, 
                 dob=None, 
                 gender=None, 
                 ):
        self.patient_id=0
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        self.dob = dob
        self.gender = gender
        self.created_on = datetime.datetime.now()

    def input_patient_details(self):
        self.name = input('Enter Patient Name: ')
        self.phone = input('Enter Patient Phone: ')
        self.email = input('Enter Patient Email: ')
        self.address = input('Enter Patient Address: ')
        self.dob = input('Enter Patient DOB (yyyy-mm-dd): ')
        self.gender = input('Enter Patient Gender (male/female): ')

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
