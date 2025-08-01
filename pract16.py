my_data = (10,20,30)
print('my_data[0]:',my_data[0])


numbers = [
    [10,20,30],
    [60,20,30],
    [90,50,10,100]
]
print('numbers[0][2]:',numbers[0][2])

message ="""
This is Awesome 
Welocome to Johns cafe
    you get happiness with good food"""

print('message')
print(message)

print("length of message", len(message))
print("message[1] is :",message[1])
print("message[-4] is :",message[-4])
print('message[len(message)-1]is:', message[len(message)-1])
print('message[-len(message)]is:', message[-len(message)])


data = list(range(10,101,10))
print("data:",data)

print(data[0:3])
print(data[0:3])
print(data[-5:-2])
print(data[ :-5])

email ="john@example.com"
name = email[0:4]
domain = email[5:]
print(email[0:4])
print(email[4:])

data1 = (10,20,30)
data2 =(40,50,60)

data3 =data1 + data2
print('data3',data3)

str1 = "my name"
str2 = " is navdeep"
str3 =str1 + str2
print("str3",str3)

data4 = data1*3
print('data4:',data4)

str4 = str1 * 3
print('str4:',str4)

data = {10,20,30,40,50}
student = {
    'roll_number':1,
    'name':'john',
    'age': 20,
    'gender':'male'
    'address':'redwood  shores '
}
print('20 in data',20 in data)

