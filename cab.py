class user:
    def __init__(self):  
        print('constructor executed')
        print('self:',self,type(self),id(self))



class resturant:
    def __init__(self):
        print('constructor executed')
        print('self:',self,type(self),id(self))


navdeep = user()
by_the_falls = resturant()
print('navdeep is : ', navdeep, type(navdeep), id(navdeep))
print('Data is object refered by navdeep:')
print(vars(navdeep))
navdeep.age = 20
navdeep.gender ='F'
print('Data is object refered by navdeep:')
print(vars(navdeep))

by_the_falls.address = 'jamalpur'
by_the_falls.timing = 9
print('Data is object refered by by_the_falls:')
print(vars(by_the_falls))
#write data in object


