"""
name,brand,price,range,hp
"""
class Car:
    def __init__(self,name,brand,price,range,hp):
        self.name = name
        self.brand = brand
        self.price = price
        self.range = range
        self.hp = hp
        self.next = None
        self.previous = None


    def user_input(self):
        self.name = input('Enter car name:')
        self.brand = input('Enter car brand:')
        self.price = float(input('Enter car price:'))
        self.range = int(input('Enter car ranger:'))
        self.hp = int(input('Enter car horse power:'))
        
    def __str__(self):
     
        car_string = """"
        ------------{}--------
        Brand : {}
        Price : {}
        Range : {}
        HP : {}
        ------------{}--------
        """.format(self.name, self.brand, self.price, self.range, self.hp)        
   
    
car = Car(name='harrier ev', brand = 'tata', price= '23.8',range = 100, hp= 420)
car.user_input()
print(car)

