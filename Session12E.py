# Circular Doubly Linked List
class FlightList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # add is going to add a flight in the linked list
    def add(self, flight):
        self.size += 1
        # print('[PlayList][add] song:', song)
        if self.head == None:
            self.head = flight
            self.tail = flight
        else:
            self.tail.next = flight
            flight.previous = self.tail
            flight.next = self.head
            self.head.previous = flight
            self.tail = flight

    def iterate(self, direction=0):

        if direction == 0:
            flight = self.head
            flight.show()
            while flight.next != self.head:
                flight = flight.next
                flight.show()
        else:
            flight = self.tail
            flight.show()
            while flight.previous != self.tail:
                flight = flight.previous
                flight.show()


    def search_by_code(self, flight_code):
        
        flag = False

        flight = self.head
        
        if flight.flight_code == flight_code:
            print('Flight Code Matched. Flight Found..')
            flight.show()
            flag = True
        else:
            while flight.next != self.head:
                flight = flight.next
                
                if flight.flight_code == flight_code:
                    print('Flight Code Matched. Flight Found..')
                    flight.show()
                    flag = True
                    break
        
        if flag == False:
            print('No Flight Matching', flight_code, 'Found...')