from Session14B import Car
from Session14C import CarList

list = CarList() # head, tail and size

car1 = Car(name='1. Harrier EV')
car2 = Car(name='2. Be6')
car3 = Car(name='3. Windsor EV')
car4 = Car(name='4. Hector EV')
car5 = Car(name='5. EV9')
car6 = Car(name='6. Nexon EV')
car7 = Car(name='7. Comet EV')

list.add(car=car1)
list.add(car=car2)
list.add(car=car3)
list.add(car=car4)
list.add(car=car5)
list.add_in_between(car1=car2, car2=car3, car=car6)
list.add_in_front(car=car7)

# list.delete(name='3. Windsor EV')
# list.delete_head()
# list.delete_tail()
print('size of list is:', list.size)

list.iterate()