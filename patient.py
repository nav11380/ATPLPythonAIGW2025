import datetime

# Model using OOPS
class Patient:

    def __init__(self, serial_no=None, 
                 name=None, 
                 phone=None, 
                 address=None, 
                 email =None, 
                 weight=None,
                 height =None
                 ):
        self.serial_no = serial_no
        self.name = name
        self.phone = phone
        self.address = address
        self.email = email
        self.weight = weight
        self.height = None

        # Automatically pickup the date time stamp
        self.date_time_stamp = str(datetime.datetime.now())

    def input_visitor_details(self):
        self.name = input('Enter Your Name: ')
        self.phone = input('Enter Your Phone: ')
        self.address = input('Enter Your Address: ')
        self.email = input('Enter Your Email: ')
        self.weight = input('Enter Your Weight: ')
        self.height = input('Enter Your Height: ')
    def __str__(self):
        # CSV String -> Comma Separated Value
        # Format for excel
        return '{},{},{},{},{},{},{}\n'.format(self.serial_no,
                                            self.date_time_stamp,
                                            self.name,
                                            self.phone,
                                            self.address,
                                            self.email,
                                            self.weight,
                                            self.height
                                            )

