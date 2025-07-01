"""
    OOPS
        Has-A Relationship between objects

        Zomato - Food Delivery App
        1 Restaurant Has 1 Menu
        1 Menu Has Many Dishes

        Many Restaurants has Many Menus/Dishes
        Many Users are Placing Many Orders

        1 to 1
        1 to many

        Object     | Attributes i.e. data associated with Object
        ------------------------------------------------------------------
        Restaurant | name, phone, email, address, rating, pricePerPerson
        Menu       | name, dishes, numberOfDishes
        Dish       | name, price, rating


        1 User can book 1 Cab (at a time)
        1 Cab has 1 Driver

        1 User can have many bookings (history)

        Object | Attributes i.e. data associated with Object
        ------------------------------------------------------------------
        User   | name, phone, email, address, gender, age
        Driver | name, phone, email, address, gender, age, licenseNumber, experience, rating
        Cab    | vehicleNumber, model, color, type, brand
        Booking| user, cab, fare, date, time, source, destinition

"""

"""

        Object     | Attributes i.e. data associated with Object
        ------------------------------------------------------------------
        Restaurant | name, phone, email, address, rating, pricePerPerson, menu
        Menu       | name, dishes, numberOfDishes
        Dish       | name, price, rating

        1 Restaurant Has 1 Menu
        1 Menu Has Many Dishes

"""

class Dish:

    # Constructor - It is used to create an object
    # it is a function
    # self is the first input, and it holds the hashcode of current object
    def __init__(self, name='NA', price=0, rating=0):
        # LHS self.name -> in the object we will create an attribute name
        # RHS name (this is the input which we can pass in the constructor as value)
        self.name = name
        self.price = price
        self.rating = rating

    # self will always be available as 1st input
    # in all the functions, created inside the class
    def show(self):
        print("------------DISH------------")
        print("Name:", self.name)
        print("Price:", self.price)
        print("Rating:", self.rating)
        print("------------DISH------------")
        print()


"""
# LHS: dish1 -> is a reference variable, which holds the hashcode for object
# RHS: Dish() -> execution of constructor with default values 
# to create an object in memory
dish1 = Dish()

# RHS: Dish(name='Paneer Tikka', price=200, rating=4.5)
# execution of constructor with custom values 
# to create an object in memory
dish2 = Dish(name='Paneer Tikka', price=200, rating=4.5)
dish3 = Dish(name='Noodles', price=150, rating=4.0)

print('dish1:', dish1)
print('dish2:', dish2)
print('dish3:', dish3)

dish1.show()
dish2.show()
dish3.show()
"""