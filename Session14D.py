from Session14B import Car
from Session14C import CarList

list = CarList() # head, tail and size

car1 = Car(name='Harrier EV')
car2 = Car(name='Be6')
car3 = Car(name='Windsor EV')

print('car1 hashcode:', id(car1))
print('car2 hashcode:', id(car2))
print('car3 hashcode:', id(car3))

list.add(car=car1)
list.add(car=car2)
list.add(car=car3)

print('list head hashcode:', id(list.head))
print('list tail hashcode:', id(list.tail))

print('car1 next hashcode:', id(car1.next))
print('car1 previous hashcode:', id(car1.previous))

print('car2 next hashcode:', id(car2.next))
print('car3 previous hashcode:', id(car2.previous))

print('car3 next hashcode:', id(car3.next))
print('car3 previous hashcode:', id(car3.previous))

list.iterate(direction=1)