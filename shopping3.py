from shopping import Product
from shopping1 import ShoppingCart

Product_1= Product("Headphones","apple", 1440, 1, 1660, "apple", 0.5, "plastic")
Product_2= Product("laptop","hp", 44440, 2, 110660, "ryzen", 0.7, "metal")

shopping_cart = ShoppingCart
shopping_cart.add_product(Product_1)
shopping_cart.add_product(Product_2)
def show_menu():
    print("------------shopping carrt menu--------")
    print("1.show cart")
    print("2.update product quantity")
    print("3.exit")

    def select_product(self,cart):
        if self.head == None:
            self.head = Product
            self.tail = Product
            Product.index = self.size
            self.size += 1
        else:
            Product.index = self.size
            self.size += 1
            self.tail.next = Product
            Product.previous = self.tail
            Product.next = self.head
            self.head.previous = Product
            self.tail = Product



