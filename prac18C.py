from prac18 import Visitor
from prac18A import Filehelper
class VistorApp:
    def __init__(self):
        print('-------------------')
        print('Welcome to vistor log app')
        print('---------------------')
        self.file_hepler = Filehelper()

    def show_menu(self):
        while True:
            print('---------------------')
            print("1.Log a visit")
            print("2.view visit log book")
            print("3.Quit")
            print('---------------------')
            choice =int(input('Enter your name:'))

            if choice == 1:
                self.add_visitor()
            elif choice == 2:
                self.view_all_visitors()
            elif choice == 3:
                print("-------------")
                print("Thank you for your visit")
                print("-------------")
                break
            else:
                print("invalid menu option")
    def add_visitor(self):
        visitor = Visitor()
        visitor.input_vistor_details()
        visitor.serial_no = self.file_hepler.lines_in_file()
        self.file_hepler.write_in_file(content= str(visitor))
    def view_all_visitors(self):
        self.file_hepler.read_file(Visitor)
        