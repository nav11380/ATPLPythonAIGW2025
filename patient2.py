from patient import Patient

# Controller
from patient1 import FileHelper

# View + Controller
class PatientApp:

    def __init__(self):
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print("Welcome to Patient Log Book App")
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        
        # Create a File Helper Object, which is an attribute of VistorApp
        # Has-A Relationship
        self.file_helper = FileHelper()
        print('File Size:', self.file_helper.file_size(), 'bytes')

    def show_menu(self):
        
        while True:
            print('~~~~~~~~~~Select Option~~~~~~~~~~')
            print("1: Log a Patient")
            print("2: View Visit Log Book")
            print("3: Quit")
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            choice = int(input('Enter Your Choice: '))

            if choice == 1:
                self.add_patient()
            elif choice == 2:
                self.view_all_patient()
            elif choice == 3:
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                print('Thank You for Using Patient App')
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                break
            else:
                print("Invalid Menu Option")

    def add_visitor(self):
        # 1. Create an Empty Visitor Object
        patient = Patient()
        # 2. Take Input
        patient.input_visitor_details()
        # 3. Save Visitor in File
        patient.serial_no = self.file_helper.lines_in_file()
        self.file_helper.write_in_file(content=str(patient))

    def view_all_patinet(self):
        self.file_helper.read_file()