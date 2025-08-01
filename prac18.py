import datetime

class Visitor:
    def __init__(self,serial_no =None, phone= None,address = None, whom_to_meet = None,purpose = None):
                self.serial_no =serial_no
                self.phone = phone
                self.address = address
                self.whom_to_meet =whom_to_meet
                self.purpose = purpose
                self.date_time_stamp = str(datetime.datetime.now())

    def input_vistor_details(self):
            self.name = input("enter your name")
            self.phone = input("enter your phone")
            self.address = input("enter your address")
            self.whom_to_meet = input("enter your whom_to_meet")
            self.purpose = input("enter your purpose")

    def __str__(self):
            return'{},{},{},{},{}\n'.format(self.serial_no,
                                            self.date_time_stamp,
                                            self.name,
                                            self.phone,
                                            self.address,
                                            self.whom_to_meet,
                                            self.purpose
                
            )