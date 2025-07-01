"""

        Object     | Attributes i.e. data associated with Object
        ------------------------------------------------------------------
        Restaurant | name, phone, email, address, rating, pricePerPerson, menu
        Menu       | name, dishes, numberOfDishes
        Dish       | name, price, rating

        1 Restaurant Has 1 Menu
        1 Menu Has Many Dishes

"""

class Restaurant:

    def __init__(self, name='NA', phone='NA', email='NA', 
                 address='NA', rating=0, price_per_person=0, menu=None):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        self.rating = rating
        self.price_per_person = price_per_person
        self.menu = menu

    def show(self):
        print("------------------------------")
        print("Name:", self.name)
        print("Phone:", self.phone)
        print("Email:", self.email)
        print("Address:", self.address)
        print("Rating:", self.rating)
        print("Price_per_person:", self.price_per_person)
        print("Menu:", self.menu)
        print("------------------------------")
        