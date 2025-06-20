# one_way_flight_booking = set()
# one_way_flight_booking = dict()
# one_way_flight_booking = list()
# one_way_flight_booking = tuple()

# Multi Line Comment in Python

"""
one_way_flight_booking = {}

one_way_flight_booking['from'] = 'Delhi'
one_way_flight_booking['to'] = 'Bengaluru'
one_way_flight_booking['traveldate'] = '25 June 2025'
one_way_flight_booking['travellers'] = 2
"""


one_way_flight_booking = {
    'from': {
        'location':'delhi',
        'description': 'DEL Delhi Airport India'
    },
    'to': 'Bengaluru',
    'traveldate': '25 June 2025',
    'travellers':  2
}

one_way_flight_booking['retuendate'] = '29 June 2025'
one_way_flight_booking['travelclass'] = 'economy'


print(one_way_flight_booking, type(one_way_flight_booking), id(one_way_flight_booking))