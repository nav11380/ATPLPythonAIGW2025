from Session10 import Dish
from Session10A import Menu
from Session10B import Restaurant


dish1 = Dish()
dish2 = Dish(name='Paneer Tikka', price=200, rating=4.5)
dish3 = Dish(name='Noodles', price=150, rating=4.0)

# List of Dishes
#          0       1      2 
dishes = [  dish1,
            dish2, 
            dish3
            ]
# print('dishes:', dishes)
# print('dihses hashcode:', id(dishes))

menu = Menu(name='Indian Menu', 
            dishes=dishes,                  # 1 to many mapping
            number_of_dishes=len(dishes))

# print(menu)

restaurant = Restaurant(name='Johns Cafe', 
                        phone='+91 99999 11111', 
                        email='johnscafe@example.com',
                        address='redwood shores',
                        rating=4.5,
                        price_per_person=500,
                        menu=menu) # 1 to 1 mapping


restaurant.show()