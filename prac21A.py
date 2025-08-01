

# Either execute directly without main (Student Life)
# app = DoctorsApp()
# app.show_main_menu()

# Or execute with main function (Professional)
# main file or driver file of the application


from prac21 import DoctorsApp  # ✅ Make sure this points to the file where DoctorsApp is defined

def main():
    app = DoctorsApp()
    app.show_main_menu()
if __name__ == '__main__':
    main()
