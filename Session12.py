"""
    Search
    Linear Search 
    1. Simple List
    2. List of Dictionary
    3. List of Objects
    4. Our Linked List
"""

data = [10, 20, 30, 40, 50]

number = int(input('Enter Number to Search: '))
# for index in range(0,len(data),1):
flag = False
for index in range(len(data)):
    if data[index] == number:
        print(number, 'found at index:', index)
        flag = True
        break

if flag == False:
    print('number not found')


names = ['john', 'jennie', 'anna', 'kim', 'ben']
name = input('Enter Name to Search: ')
index = 0
found = 0

while index < len(names):
    
    if names[index] == name:
        print(name, 'found at index:', index)
        found = 1
        break
    
    index+=1

if found == 0:
    print('name not found')


