"""
    STACK:
    PUSH -> add in end
    POP  -> delete from tail
    Iterate -> tail to head
"""

# Circular Doubly Linked List
# As STACK
class CarStack:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # add is going to add a car in the linked list
    def push(self, car):
        
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

    def iterate(self):
        car = self.tail
        print(car)
        while car.previous != self.tail:
            car = car.previous
            print(car)
   
    def pop(self):
        # delete tail
        self.tail = self.tail.previous
        self.tail.next = self.head
        self.head.previous = self.tail
        self.size -= 1