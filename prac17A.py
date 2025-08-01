students = {
    101: 'John',
    201: 'Jennie',
    501: 'Sia',
    99: 'Joe',
    25: 'Kim',
    201: 'Anna',
    21: 'Joe',
}
months_list = ['jan', 'feb', 'mar', 
              'apr', 'may', 'june', 
              'july', 'aug', 'sep', 
              'oct', 'nov', 'dec']

# How to create a dictionary with list, having keys as elements of list
college_attendance = {}.fromkeys(months_list, 100)
print('college_attendance')
print(college_attendance)

college_attendance['jan'] -= 5

print('college_attendance')
print(college_attendance)

keys = list(students.keys())
values = list(students.values())
items = list(students.items())

keys = list(students.keys())
attendance = {}.fromkeys(months_list, 100)
attendance_record = {}.fromkeys(keys,attendance)

