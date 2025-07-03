from Session12D import Flight
from Session12E import FlightList

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

flights = FlightList()
flights.add(flight1)
flights.add(flight2)
flights.add(flight3)
flights.add(flight4)
flights.add(flight5)


# flights.iterate()
flights.search_by_code(flight_code=input('Enter Flight Code: '))

"""
HW:
In all the logics, implement filter function
"""