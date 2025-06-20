# VIEW -> Interface
# Interface is one, with which user interacts

from_location = input('Enter from Location: ')
print('You entered:', from_location)
print(type(from_location))

travelers = int(input('Enter Number Of Travelers: '))
print('You entered:', travelers)
print(type(travelers))

feedback = float(input('Enter Your Feedback (1-5) '))
print('You entered:', feedback)
print(type(feedback))

flight_booking = {
    'from': from_location,
    'travelers': travelers,
    'feedback': feedback
}

print(flight_booking, type(flight_booking))