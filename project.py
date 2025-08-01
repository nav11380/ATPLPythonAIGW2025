class flight:

    def __init__(self, carrier='NA', flight_code='NA', source='NA', destinition='NA', departure_time='NA', arrival_time='NA', duration=0, fare=0):
        self.carrier = carrier
        self.flight_code = flight_code
        self.source = source
        self.destinition = destinition
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.duration = duration
        self.fare = fare
        self.next = None
        self.prev = None


    def show_flight_info(self):
        print('~~~~~~~~~~~~~~',self.flight_code,'~~~~~~~~~~~~~~~')
        print('carrier:',self.carrier)
        print('flight_code:', self.flight_code)
        print('source:', self.source, '| destinition:', self.destinition)
        print('departure_time:', self.departure_time, '| arrival_time:', self.arrival_time)
        print('duration:', self.duration, 'hours')
        print('fare: \u20b9', self.fare)
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print()
