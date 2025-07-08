# Circular Doubly Linked List
class CarList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # add is going to add a car in the linked list
    def add(self, car):
        

        if self.head == None:
            self.head = car
            self.tail = car
            car.index = self.size
            self.size += 1
        else:
            car.index = self.size
            self.size += 1
            self.tail.next = car
            car.previous = self.tail
            car.next = self.head
            self.head.previous = car
            self.tail = car

    def iterate(self, direction=0):

        if direction == 0:
            car = self.head
            print(car)
            while car.next != self.head:
                car = car.next
                print(car)
        else:
            car = self.tail
            print(car)
            while car.previous != self.tail:
                car = car.previous
                print(car)


    def delete(self, name):
        
        car = self.head
        
        if car.name == name:
            car.previous.next = car.next
            car.next.previous = car.previous
            self.size -= 1
            del car
        
        while car.next != self.head:
            car = car.next
            if car.name == name:
                car.previous.next = car.next
                car.next.previous = car.previous
                self.size -= 1
                del car
                break
            

    def delete_head(self):
        # New Head
        self.head = self.head.next
        self.head.previous = self.tail
        self.tail.next = self.head
        self.size -= 1

    def delete_tail(self):
        # New tail
        self.tail = self.tail.previous
        self.tail.next = self.head
        self.head.previous = self.tail
        self.size -= 1

    def add_in_front(self, car):
        car.next = self.head
        self.head.previous = car
        car.previous = self.tail
        self.head = car
        self.tail.next = self.head
        self.size += 1

    def add_in_between(self, car1, car2, car):
        car.next = car2
        car.previous = car1
        car1.next = car
        car2.previous = car
        self.size += 1

    def bubble_sort(self):
        pass

"""
    Pro: Write Logic to Maintain Index
         Then do Bubble Sort
"""