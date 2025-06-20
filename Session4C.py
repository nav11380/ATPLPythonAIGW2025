flight_booking = {
    'from': input('Enter From Location: '),
    'to': input('Enter To Location: '),
    'travelers': int(input('Enter Travelers: ')), 
    'feedback': float(input('Enter Feedback: ')) 
}

print(flight_booking, type(flight_booking))