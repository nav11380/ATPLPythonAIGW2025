class User:

    def __init__(self, id, name, phone):
        # Protected      (accessible outside the class)
        self._id = id

        # Regular/Public  (accessible outside the class)
        self.name = name 

        # Private (not accessible outside the class)
        self.__phone = phone

    def show(self):
        print(self._id, self.name, self.__phone)


user = User(id=101, name='John', phone='9876512345')
user.show()

# print(user.name)
# print(user._id)
# print(user.__phone) # error

print(user._User__phone)

print(vars(user))