"""
    Think of an Object

    Visitor: serial_no, date_time_stamp, name, phone, address, whome_to_meet, purpose
    Customer: name, phone, email, address, points
    Patient: name, phone, email, address, weight, height, bp_high, bp_low, sugar
    
    Your Own Choice

"""
import datetime

# Model using OOPS
class Visitor:

    def __init__(self, serial_no=None, 
                 name=None, 
                 phone=None, 
                 address=None, 
                 whome_to_meet=None, 
                 purpose=None):
        self.serial_no = serial_no
        self.name = name
        self.phone = phone
        self.address = address
        self.whome_to_meet = whome_to_meet
        self.purpose = purpose

        # Automatically pickup the date time stamp
        self.date_time_stamp = str(datetime.datetime.now())

    def input_visitor_details(self):
        self.name = input('Enter Your Name: ')
        self.phone = input('Enter Your Phone: ')
        self.address = input('Enter Your Address: ')
        self.whome_to_meet = input('Enter Person to Meet: ')
        self.purpose = input('Enter Purpose of your Meeting: ')
        
    def __str__(self):
        # CSV String -> Comma Separated Value
        # Format for excel
        return '{},{},{},{},{},{},{}\n'.format(self.serial_no,
                                            self.date_time_stamp,
                                            self.name,
                                            self.phone,
                                            self.address,
                                            self.whome_to_meet,
                                            self.purpose
                                            )

