"""
    Object Oriented Programming Structure
    OOPS

    1. In real world
        Object
            Anything which exists is an object
            A real thing
            An entity
        Class
            Drawing of an object

        Principle of OOPS
        1. Think of an Object
        2. Create its Representation/drawing i.e. Class
        3. From Class create a real object

    2. in computer science
        Object
            is a storage container (Box)
            which we can customize as per our requirements

        Class
            textual representation of object
            i.e. we code to create a class

        
"""

"""
Principle of OOPS
    1. Think of an Object
        OneWayFlightBooking
            from, to, departure, travelers etc

        2. Create its Representation/drawing i.e. Class


        3. From Class create a real object

"""

# 2. Representation of Object
class OneWayFlightBooking:

    # init is a function
    # constructor
    def __init__(self):
        self.from_location = 'Delhi'
        self.to_location = 'Banglore'
        self.departure = '30th June, 2025'
        self.travelers = 3


class Student:

    # init is a function
    # constructor
    def __init__(self):
        self.roll_number = 101
        self.name = 'John'
        self.phone = '+91 98765 12345'
        self.email = 'john@example.com'
        self.age = 12


# 3. Create a Real Object in Memory
# Obejct Construction Statement
ishants_flight_booking = OneWayFlightBooking()
print(ishants_flight_booking)


john_student = Student()
print(john_student)







