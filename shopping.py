class Product:
    def __init__(self, productname, brand, price, quantity, toatl_price, manufacturer, weight, material ):
        self.productname = productname
        self.brand = brand
        self.price = price
        self.quantity = quantity
        self.total_price = toatl_price
        self.manufacturer = manufacturer
        self.weight = weight
        self.material = material
        self.prev = None
        self.next = None

    def show(self):
        print('~~~~~~~~~~~~~~',self.productname,'~~~~~~~~~~~~~~~')
        print('productname:', self.productname)
        print('price  :', self.price)
        print('total_price:', self.total_price)
        print('manufacturer:', self.manufacturer)
        print('weight', self.weight)
        print('material', self.material)
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print()
        
    def update_quantity(self,new_quantity):
        if new_quantity < 0:
            print("quntity cannot be neagtive.")
        self.quantity = new_quantity

    