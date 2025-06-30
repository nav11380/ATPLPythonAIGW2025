"""
    Requirement:
    Mr. John is my client.
    He is a running a restaurant.
    He wants to build an online food delivery system.

    In my application, user should be able to login.
    he can select a restaurant.
    he can view its menu.
    Add dishes to cart and then place an oder.

    ..
    .....

    1. Identify the object, i.e. Think of Object
    
    User - name, phone, email, address, gender, age etc...
    DeliveryAgent - name, phone, email, address, gender, age, vehicleNumber, rating etc..
    Restaurant - name, image, phone, email, address, rating, operatingHours, pricePerPerson etc..
    Menu - dishes, category, totalDishes etc...
    Dish - name, image, price, rating etc..
    Order - dishes, user, deliveryAddress, restaurant, deliveryAgent

    1 User can place many orders
    1 restaurant can have many dishes
    many users can place many orders..

    etc etc etc

"""

# 2. Create Class for the Object
# User - name, phone, email, address, gender, age
# Restaurant - name, image, phone, email, address, rating, operatingHours, pricePerPerson etc..


class User:
    
    # In python, __init__ is constructor and it remains in all the classes in python
    # self is an input to __init__ (i.e. an argument)
    # Use Proper Indenetation (tab space after : )
    def __init__(self):
        print('constructor executed')
        print('self:', self, type(self), id(self))


class Restaurant:
    
    def __init__(self):
        print('constructor executed')
        print('self:', self, type(self), id(self))


#  3. Create Objects in Memory using Class
# Object Construction Statement
# LHS: john is a reference variable, it will hold the hashcode of object in RAM
# RHS: User() is creation of an object, which automatically executes __init__ (constructor)
#      Here, an empty box will be created in the RAM (Heap Area)
john = User()
fionna = User()

# Reference Copy Operation
johnnie = john


# mc_donalds = Restaurant()

print('john:', john, type(john), id(john))
print('johnnie:', johnnie, type(johnnie), id(johnnie))
print('fionna:', fionna, type(fionna), id(fionna))

# print('mc_donalds:', mc_donalds, type(mc_donalds), id(mc_donalds))


# Write data in object
# name, phone, email, address, gender, age
john.name = 'John Watson'
john.phone = '+91 99999 11111'
johnnie.email = 'john@example.com'
johnnie.address = 'redwood shores'
john.gender = 'male'
john.age = 30


fionna.name = 'Fionna Flynn'
fionna.phone = '+91 99999 22222'
fionna.email = 'fionna@example.com'
fionna.address = 'country homes'
fionna.gender = 'female'
fionna.age = 28

# Update Operation
johnnie.age = 45

# Delete Attribute Operation
del john.gender
del johnnie.address

# Delete Object
del john
del johnnie

# Read Operation

# print('data in john')
# print(vars(john))

# print('data in johnnie')
# print(vars(johnnie))

print('data in fionna')
print(vars(fionna))


# On Object we can perfrom
# 1. Create/Write
# 2. Update
# 3. Delete
# 4. Read

# CRUD operations


