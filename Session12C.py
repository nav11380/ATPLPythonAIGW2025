"""
OOPS:
1. Think of Object First
Flight | carrier, flight_code, source, destinition, departure, arrival, duration, fare

"""

# 2. Create its class

class Flight:

    def __init__(self, carrier, flight_code, source, destinition, departure, arrival, duration, fare):
        self.carrier = carrier
        self.flight_code = flight_code
        self.source = source
        self.destinition = destinition
        self.departure = departure
        self.arrival = arrival
        self.duration = duration
        self.fare = fare

    def show(self):
        print('~~~~~~~~~~~~~~',self.flight_code,'~~~~~~~~~~~~~~~')
        print('carrier:', self.carrier)
        print('source:', self.source, '| destinition:', self.destinition)
        print('departure:', self.departure, '| arrival:', self.arrival)
        print('duration:', self.duration, 'hours')
        print('fare: \u20b9', self.fare)
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print()


flight1 = Flight(
    carrier='indigo',
    flight_code='6e642',
    source='chandigarh',
    destinition='mumbai',
    departure='05:50',
    arrival='08:20',
    duration=2.3,
    fare=6499
)

flight2 = Flight(
    carrier='air india',
    flight_code='ai2660',
    source='chandigarh',
    destinition='mumbai',
    departure='17:50',
    arrival='20:45',
    duration=2.5,
    fare=7260
)

flight3 = Flight(
    carrier='indigo',
    flight_code='6e5234',
    source='chandigarh',
    destinition='mumbai',
    departure='16:30',
    arrival='19:05',
    duration=2.3,
    fare=7649
)

flight4 = Flight(
    carrier='air india',
    flight_code='ai522',
    source='chandigarh',
    destinition='bengaluru',
    departure='16:30',
    arrival='19:30',
    duration=3.0,
    fare=6606
)


flight5 = Flight(
    carrier='indigo',
    flight_code='6e6634',
    source='chandigarh',
    destinition='bengaluru',
    departure='08:25',
    arrival='11:30',
    duration=3.5,
    fare=6867
)

# List of Flight Objects
flights = [flight1, flight2, flight3, flight4, flight5]

# for index in range(len(flights)):
#     flights[index].show()


def search(flights, flight_code):
    
    flag = False
    for index in range(len(flights)):
        if flights[index].flight_code == flight_code:
            print(flight_code, 'found at index:', index)
            flights[index].show()
            flag = True
            break

    if flag == False:
        print('flight_code', flight_code,'not found')

search(flights, 'ai522')