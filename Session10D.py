from Session10 import Dish
from Session10A import Menu
from Session10B import Restaurant

restaurant = Restaurant(
                        name='Johns Cafe', 
                        phone='+91 99999 11111', 
                        email='johnscafe@example.com',
                        address='redwood shores',
                        rating=4.5,
                        price_per_person=500,
                        menu = Menu(
                                    name='Indian Menu', 
                                    dishes = [
                                                Dish(), 
                                                Dish(name='Paneer Tikka', price=200, rating=4.5), 
                                                Dish(name='Noodles', price=150, rating=4.0)
                                            ],                
                                    number_of_dishes=3
                                )
                        )


restaurant.show()


"""
Restaurant(
                        name='Johns Cafe', 
                        phone='+91 99999 11111', 
                        email='johnscafe@example.com',
                        address='redwood shores',
                        rating=4.5,
                        price_per_person=500,
                        menu = Menu(
                                    name='Indian Menu', 
                                    dishes = [
                                                Dish(), 
                                                Dish(name='Paneer Tikka', price=200, rating=4.5), 
                                                Dish(name='Noodles', price=150, rating=4.0)
                                            ],                
                                    number_of_dishes=3
                                )
                        ).show()

"""