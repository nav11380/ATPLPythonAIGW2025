"""
    Requirement:
    Mr. John is my client.
    He is wants to build a cab booking solution

    In my application, user should be able to login.
    he can select a source and destinion location.
    he can view different cabs
    he can book a cab, which allocates him nearby driver
    he can pay online or in cash
    ..
    .....

    1. Identify the object, i.e. Think of Object
    
    User - name, phone, email, address, gender, age etc...
    CabDriver - name, phone, email, address, gender, age, vehicleNumber, rating etc..
    Cab - vehicleNumber, color, model, type, companyBrand etc..
    Booking - user, cab, cabDriver, date, time, fare, paymentMode etc etc..

    1 User can book many cabs
    1 User at 1 time can have 1 booking
    many users can book many cabs

"""

# 2. Create Class for the Object

class Cab:
    
    # self is a reference variable
    # it is mandatory as 1st parameter in construcor or any other function in class
    # self will have the hashcode of the object in use
    def __init__(self):
        print('constructor executed')
        print('self:', self, type(self), id(self))


johns_cab = Cab()
print('johns_cab:', johns_cab, type(johns_cab), id(johns_cab))

print('Data in Object Referred by johns_cab')
print(vars(johns_cab))

# vehicleNumber, color, model, type, companyBrand
johns_cab.vehicleNumber = 'PB10AL4433'
johns_cab.color = 'black'
johns_cab.model = 'Swift Dezire'
johns_cab.type = 'Sedan'
johns_cab.companyBrand = 'Maruti'

print('Data in Object now')
print(vars(johns_cab))