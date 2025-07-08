"""
    QUEUE:
    Enqueue -> add in end
    Dequeue  -> delete from head
    Iterate -> head to tail
"""

# Circular Doubly Linked List
# As STACK
class CarQueue:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # add is going to add a car in the linked list
    def enqueu(self, car):
        
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
        car = self.head
        print(car)
        while car.next != self.head:
            car = car.next
            print(car)
   
    def dequeue(self):
        # delete head
        self.head = self.head.next
        self.head.previous = self.tail
        self.tail.next = self.head
        self.size -= 1