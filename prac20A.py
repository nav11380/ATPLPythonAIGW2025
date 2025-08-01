"""
DoctorsApp
"""
import datetime
from ATPLPythonAIGW2025.patient import Patient
from Session20 import DBHelper
class DoctorsApp:
    def __init__(self):
        print("-------------------")
        print("Welcome to Doctors App")
        print("App started at:", datetime.datetime.now())
        print("-------------------")


    def show_main_menu(self):
        while True:
            print('Main Menu:')
            print('1:Patient')
            print('2.Consulatation')
            print('3.Quit') 
            choice = int(input('Enter Your Choice:'))

            if choice == 1:
                self.show_patient_menu()
            elif choice == 2:
                self.show_consultation_menu()
            elif choice == 3:
                pass 
                print('-----------------')
                print('Thank you for using the App')
                print('App closed at:', datetime.datetime.now())
                print('-----------------')
                break
            else:
                print('enter more suitable option')

    def show_patient_menu(self):

        print('~~~~~~~~~~~~~~~~~~~~~~')
        print('Patient Menu Opened')
        print('~~~~~~~~~~~~~~~~~~~~~~')

        while True:
            print('Patient Menu: ')
            print('1: Add New Patient')
            print('2: Update Existing Patient')
            print('3: Delete Existing Patient')
            print('4: Fetch All Patients')
            print('5: Fetch Patient by Phone Number')
            print('6: Fetch Male Patients')
            print('7: Fetch Female Patients')
            print('8: Fetch Patients by Created On Date (Sort)')
            print('9: Quit')
            choice = int(input('Enter Your Choice: '))
            
            if choice == 1:
                pass
            elif choice == 2:
                pass
            elif choice == 3:
                pass
            elif choice == 4:
                pass
            elif choice == 9:
                print('~~~~~~~~~~~~~~~~~~~~~~')
                print('Patient Menu Closed')
                print('~~~~~~~~~~~~~~~~~~~~~~')
                break
            else:
                print('Enter Suitable Menu Option...')

    def show_consultation_menu(self):

        print('~~~~~~~~~~~~~~~~~~~~~~~~')
        print('Consultation Menu Opened')
        print('~~~~~~~~~~~~~~~~~~~~~~~~')

        while True:
            print('Consultation Menu: ')
            print('1: Add New Consultation')
            print('2: Update Existing Consultation')
            print('3: Delete Existing Consultation')
            print('4: Fetch All Consultation')
            print('5: Fetch Consultation of a Patient')
            print('6: Quit')
            choice = int(input('Enter Your Choice: '))
            
            if choice == 1:
                pass
            elif choice == 2:
                pass
            elif choice == 3:
                pass
            elif choice == 4:
                pass
            elif choice == 6:
                print('~~~~~~~~~~~~~~~~~~~~~~~~')
                print('Consultation Menu Opened')
                print('~~~~~~~~~~~~~~~~~~~~~~~~')
                break
            else:
                print('Enter Suitable Menu Option...')

        