flight1 = {
    'carrier': 'indigo',
    'flight_code': '6E633',
    'from' : 'chandigarh',
    'to': 'delhi',
    'departure': "5.50",
    'arrival': '08:20',
    'duration' : '02:20',
    'fare': 6255
    }
flight2= {
    'carrier': 'air india ',
    'flight_code': '6E55',
    'from' : 'chandigarh',
    'to': 'mumbai',
    'departure': "6.50",
    'arrival': '09:20',
    'duration' : '03:20',
    'fare': 7255
    }
flight3 = {
    'carrier': 'indigo',
    'flight_code': '4E55',
    'from' : 'chandigarh',
    'to': 'goa',
    'departure': "9.50",
    'arrival': '09:20',
    'duration' : '11:20',
    'fare': 9255
    }
flight4 = {
    'carrier': 'indigo',
    'flight_code': '5E633',
    'from' : 'chandigarh',
    'to': 'banglore',
    'departure': "6.50",
    'arrival': '03:20',
    'duration' : '04:20',
    'fare': 9255
    }

flights =[flight1, flight2, flight3, flight4]

source = input('enter source location')
destination = input('enter source destination')

for index in range(len(flights)):
    if flights[index]['from'] == source and flights[index]['to'] == destination:
        print(flights[index])

def search(flight,fligh_code):
    for index in range(len(flight)):
        