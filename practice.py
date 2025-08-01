class Menu:
    def __init__(self, name = 'NA', dishes = [] , number_of_dishes = 0):
        self.name = name
        self.dishes = dishes
        self.number_of_dishes = number_of_dishes 
    
    def show(self):
        print('-----------')
        print('name',self.name )
        print('dishes',self.dishes )
        print('number_of_dishes',self.number_of_dishes )
        print('---------')


