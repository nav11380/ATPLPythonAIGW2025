"""

        Object     | Attributes i.e. data associated with Object
        ------------------------------------------------------------------
        Restaurant | name, phone, email, address, rating, pricePerPerson, menu
        Menu       | name, dishes, numberOfDishes
        Dish       | name, price, rating

        1 Restaurant Has 1 Menu
        1 Menu Has Many Dishes

"""

class Menu:

    def __init__(self, name='NA', dishes=[], number_of_dishes=0):
        self.name = name
        self.dishes = dishes
        self.number_of_dishes = number_of_dishes

    def show(self):
        print("~~~~~~~~~~~~~MENU~~~~~~~~~~~~~~")
        print("Name:", self.name)
        # print("Dishes:", self.dishes)
        
        print("Dishes")
        for index in range(len(self.dishes)):
            self.dishes[index].show()

        print("number_of_dishes:", self.number_of_dishes)
        print("~~~~~~~~~~~~~MENU~~~~~~~~~~~~~~")
        