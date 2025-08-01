class ShoppingCart:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def add(self, product):
        self.size += 1
        if self.head is None:
            self.head = product
            self.tail = product
            product.next = product
            product.prev = product
        else:
            product.previous = self.tail
            product.next = self.head
            self.tail.next = product
            self.head.prev = product
            self.tail = product
    
    def show(self):
        if self.head is None:
            return("shopping cart is empty")
        
        current = self.head
        while True:
            current.show()
            current = current.next
            if current == self.head:
                break

    def remove_product(self,product):
        if self.head is None:
            return
        if self.head == self.tail and self.head == product:
            self.head= None
            self.tail = None
            self.size = 0
            return
        current = self.head
        while True:
            if current == product:
                current.prev.next = current.next
                current.next.prev = current.prev
                if current == self.head:
                    self.head = current.next
                if current == self.tail:
                    self.tail = current.prev
                self.size -= 1
                break
            current = current.next
            if current == self.head:
                break
    
    def update(self, product, quantity):
        if quantity < 0:
            print("qunatity cannot be neagtive")
            return
        if quantity == 0:
            print("product removed from the cart.")
        else:
            print("product qunaity  updated to qunatity")

     



            
