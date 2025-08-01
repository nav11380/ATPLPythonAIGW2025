flight1 = {
    'carrier': 'indigo',
    'flight_code': '6e642',
    'from': 'chandigarh',
    'to': 'mumbai',
    'departure': '05:50',
    'arrival': '08:20',
    'duration': 2.3,
    'fare': 6499
}

flight2 = {
    'carrier': 'air india',
    'flight_code': 'ai2660',
    'from': 'chandigarh',
    'to': 'mumbai',
    'departure': '17:50',
    'arrival': '20:45',
    'duration': 2.5,
    'fare': 7260
}

flight3 = {
    'carrier': 'indigo',
    'flight_code': '6e5234',
    'from': 'chandigarh',
    'to': 'mumbai',
    'departure': '16:30',
    'arrival': '19:05',
    'duration': 2.3,
    'fare': 7649
}

flight4 = {
    'carrier': 'air india',
    'flight_code': 'ai522',
    'from': 'chandigarh',
    'to': 'bengaluru',
    'departure': '16:30',
    'arrival': '19:30',
    'duration': 3.0,
    'fare': 6606
}

flight5 = {
    'carrier': 'indigo',
    'flight_code': '6e6634',
    'from': 'chandigarh',
    'to': 'bengaluru',
    'departure': '08:25',
    'arrival': '11:30',
    'duration': 3.5,
    'fare': 6867
}

def filter (source, destination, need_Departure_from,need_Departure_to):
    flight = self.head 
    while flight.next != self.head:
        
        if(flight.source== source and flight.destionation == destination and need_Departure_to > flight.departure > need_Departure_from):
            print("here are flights available as per your requirements:")
            flight.show()
            flight = flight.next
            if flight == self.head:
                break

def search_by_code (self, flight_code):

