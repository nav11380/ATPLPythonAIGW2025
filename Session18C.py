"""
Application
"""

class VisitorApp:

    def __init__(self):
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print("Welcome to Visitor Log Book App")
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

    def show_menu(self):
        
        while True:
            print('~~~~~~~~~~Select Option~~~~~~~~~~')
            print("1: Log a Visit")
            print("2: View Visit Log Book")
            print("3: Quit")
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            choice = int(input('Enter Your Choice: '))


            if choice == 1:
                print("Add A new Visitor Log..")
            elif choice == 2:
                print("Read All Visitor Logs..")
            elif choice == 3:
                break
            else:
                print("Invalid Menu Option")

