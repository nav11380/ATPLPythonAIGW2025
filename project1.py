from project import flight
 
class flightlist:
    def __init__(self,name):
       self.list_of_flights = []

    def add_flight(self):
        carrier = input("enter carrier:")
        flight_code = input('enter flight code:')
        arrival = input('enter arrival time:')
        departure = input('enter  departure:')
        duration = input('enter durationr:')
        source = input('enter   source :')
        destination = input('enter destination:')
        new_flight = flight(carrier, flight_code, arrival, departure, duration, source, destination)
        self.list_of_flights.append(new_flight)
        print("flight added successfully")

    def delete_flights(self,given_code):
        found = False
        for i, flight in enumerate(self.list_of_flights):
            if flight.flight_code == given_code:
                found = True
                del self.list_of_flights[i]
                break
        if not found:
            print("no such flights found")

    def display_all(self):
        print("--------------------all the flights are---------")
        for flights in self.list_of_flights:
            flight.show_flight_info()



        if self.head is None:
            self.head = self.head = flight 
            flight.next = flight.prev = flight
        else:
            flight.previou
            s = self.tail
            flight.next = self.head
            self.tail.next = flight
            self.head.prev = flight
            self.tail = flight
        self.size != 1
    
    def search_flight(self,given_code):
        flag = False
        for flight in self.list_of_flights:
            if flight.flight_code == given_code:
                flag = True
                break
        if flag == False:
            print("flight not found ")

    def finding_flights(self, given_source, given_destination ):
       found = False
       print("-----------Flights are given below----------")
       for flight in self.list_of_flights:
            if (found.source.lower() == given_source.lower() and flight.destination.lower() == given_destination.lower()):
                found = True
                flight.show_flights_info()
            if not found:
                print("no flights found")

flight1 = flight(
    carrier='indigo',
    flight_code='6e642',
    source='chandigarh',
    destinition='mumbai',
    departure_time='05:50',
    arrival_time='08:20',
    duration=2.3,
    fare=6499
)

flight2 = flight(
    carrier='air india',
    flight_code='ai2660',
    source='chandigarh',
    destinition='mumbai',
    departure_time='17:50',
    arrival_time='20:45',
    duration=2.5,
    fare=7260
)

flight3 = flight(
    carrier='indigo',
    flight_code='6e5234',
    source='chandigarh',
    destinition='mumbai',
    departure_time ='16:30',
    arrival_time='19:05',
    duration=2.3,
    fare=7649
)

flight4 = flight(
    carrier='air india',
    flight_code='ai522',
    source='chandigarh',
    destinition='bengaluru',
    departure_time ='16:30',
    arrival_time='19:30',
    duration=3.0,
    fare=6606
)


flight5 = flight(
    carrier='indigo',
    flight_code='6e6634',
    source='chandigarh',
    destinition='bengaluru',
    departure_time='08:25',
    arrival_time='11:30',
    duration=3.5,
    fare=6867
)


flight_list1 = flightlist("local flights")
flight_list1.list_of_flights = [flight1,flight2,flight3,flight4,flight5]
flight_list1.display_all


