

# List of Months
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