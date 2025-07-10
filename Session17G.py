# Think of Object
# Visitor: name, phone, purpose, meet_to

class Visitor:
    
    def __init__(self, name=None, phone=None, purpose=None, meet_to=None):
        self.name = name
        self.phone = phone
        self.purpose = purpose
        self.meet_to = meet_to


    def add_visitor(self):
        self.name = input('Enter Your Name: ')
        self.phone = input('Enter Your Phone: ')
        self.purpose = input('Enter Your Purpose to Meet: ')
        self.meet_to = input('Enter Name of Person, you wish to meet: ')

    def to_csv(self):
        # csv = '{},{},{},{}\n'.format(self.name, self.phone, self.purpose, self.meet_to)
        # return csv
        return '{},{},{},{}\n'.format(self.name, self.phone, self.purpose, self.meet_to)
        

