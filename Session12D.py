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
        self.next = None
        self.previous = None

    def show(self):
        print('~~~~~~~~~~~~~~',self.flight_code,'~~~~~~~~~~~~~~~')
        print('carrier:', self.carrier)
        print('source:', self.source, '| destinition:', self.destinition)
        print('departure:', self.departure, '| arrival:', self.arrival)
        print('duration:', self.duration, 'hours')
        print('fare: \u20b9', self.fare)
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print()