"""
class Shoe:
    def __init__(self, code, name, brand, price, size):
        self.code = code
        self.name = name
        self.brand = brand
        self.price = price
        self.size = size

        def show(self):
            print('------Shoe Details------')
            print(self.code)
            print(self.name)
            print(self.brand)
            print(self.price)
            print(self.size)
            print('------Shoe Details------')

class MobilePhone:
    def __init__(self, code, name, brand, price, screen_size, os, memory, ram):
        self.code = code
        self.name = name
        self.brand = brand
        self.price = price
        self.screen_size = screen_size
        self.os = os
        self.memory = memory
        self.ram = ram

        def show(self):
            print('------MobilePhone Details------')
            print(self.code)
            print(self.name)
            print(self.brand)
            print(self.price)
            print(self.screen_size)
            print(self.os)
            print(self.memory)
            print(self.self.ram)
            print('------MobilePhone Details------')

class TV:
    def __init__(self, code, name, brand, price, screen_size, screen_technology):
        self.code = code
        self.name = name
        self.brand = brand
        self.price = price
        self.screen_size = screen_size
        self.screen_technology = screen_technology


        def show(self):
            print('------TV Details------')
            print(self.code)
            print(self.name)
            print(self.brand)
            print(self.price)
            print(self.screen_size)
            print(self.screen_technology)
            print('------TV Details------')
"""

class Product:

    def __init__(self, code, name, brand, price):
        self.code = code
        self.name = name
        self.brand = brand
        self.price = price

    def show(self):
        print('------Product Details------')
        print(self.code)
        print(self.name)
        print(self.brand)
        print(self.price)
        print('------Product Details------')

# Inheritance Relationship -> Shoe is a child of Product
class Shoe(Product):
    def __init__(self, code, name, brand, price, size):
        Product.__init__(self, code, name, brand, price)
        self.size = size

    def show(self):
        print('------Shoe Details------')
        Product.show(self) # Accessing Parent's Function
        print(self.size)
        print('------Shoe Details------')

class MobilePhone(Product):
    def __init__(self, code, name, brand, price, screen_size, os, memory, ram):
        Product.__init__(self, code, name, brand, price)
        self.screen_size = screen_size
        self.os = os
        self.memory = memory
        self.ram = ram

    def show(self):
        print('------MobilePhone Details------')
        Product.show(self) # Accessing Parent's Function
        print(self.screen_size)
        print(self.os)
        print(self.memory)
        print(self.ram)
        print('------MobilePhone Details------')


alphaboost = Shoe(code=101, name='Alphaboost', brand='Adidas', price=5000, size=9)
phone = MobilePhone(code=201, name='iphone', brand='apple', price=80000, screen_size=5, os='ios', memory=128, ram=4)

alphaboost.show()
phone.show()

"""
    Single Level
    A
    |
    B

    Multi Level
    A
    |
    B
    |
    C

    class A:
        pass

    class B(A):
        pass

    class C(B):
        pass
        
    
    Hierarchy
    A
    |
  B C D

    Multiple

    A B
     |
     C

    Hybrid
    A
    |
    B
    |
 C     D
    |
    E

"""