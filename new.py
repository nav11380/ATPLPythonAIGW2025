"""
nykaa -online beauty app
1.one  may have one email
2.it has many products

object | attributes data associated with object
user   | user id, username, password, email id ,phone number
product| product id,product price,product avilability

"""
class Dish:
    def __init__(self, name= 'NA', price=0, rating=0):
        self.name = name
        self.price = price
        self.rating = rating
    
    def show(self):
        print('------------')
        print('name',self.name)
        print('price',self.price)
        print('rating',self.rating)

dish1 = Dish()
dish2 = Dish(name ='paneer tikka ',price=200, rating=4):

print('dish1',dish1)
print('dish2',dish2)

dish1.show()
dish2.show()