"""
    DoctorsApp
"""

# View + Controller

import datetime

from prac21B import DBHelper
from Session19A import Patient
from Session19B import Consultation

class DoctorsApp:

    def __init__(self):
        print('~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('Welcome to Doctors App')
        print('App Started at: ', datetime.datetime.now())
        print('~~~~~~~~~~~~~~~~~~~~~~~~~')

        self.db_helper = DBHelper(
            user='user',
            password='password',
            host='host',
            database='datbase'
        )



    def show_main_menu(self):

        while True:

            print('~~~~~~~~~~~~~~~~~~~~~')
            print('Main Menu: ')
            print('1: Patient')
            print('2: Consulatation')
            print('0: Quit')
            print('~~~~~~~~~~~~~~~~~~~~~')

            choice = int(input('Enter Your Choice: '))
            
            if choice == 1:
                self.show_patient_menu()
            elif choice == 2:
                self.show_consultation_menu()
            elif choice == 0:
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                print('Thank You for using Doctors App')
                print('App Closed at: ', datetime.datetime.now())
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                self.db_helper.close()
                break
            else:
                print('Enter Suitable Menu Option...')


    def show_patient_menu(self):

        print('~~~~~~~~~~~~~~~~~~~~~~')
        print('Patient Menu Opened')
        print('~~~~~~~~~~~~~~~~~~~~~~')

        while True:
            # menu_string = """Patient Menu: 
            # 1: Add New Patient
            # 2: Update Existing Patient
            # """
            # print(menu_string)
            print('Patient Menu: ')
            print('1: Add New Patient')
            print('2: Update Existing Patient')
            print('3: Delete Existing Patient')
            print('4: Fetch All Patients')
            print('5: Fetch Patient by Phone Number')
            print('6: Fetch Male Patients')
            print('7: Fetch Female Patients')
            print('8: Fetch Patients by Created On Date (Sort)')
            print('0: Quit')
            choice = int(input('Enter Your Choice: '))
            
            if choice == 1:
                patient = Patient()
                patient.input_patient_details()
                sql_query = "insert into Patient values(null, '{}', '{}', '{}','{}', '{}', '{}', '{}')".format(
                    patient.name,
                    patient.phone,
                    patient.email,
                    patient.address,
                    patient.dob,
                    patient.gender,
                    patient.created_on
                )
                self.db_helper.write(sql_query)

            elif choice == 2:
                # Update Patient
                # 1. Fetch the Existing Patient
                patient_id = input('Enter Patient Id to Update Details: ')
                # Before i Update, i will fetch the exiting patient details
                sql_query = "select * from Patient where patient_id = '{}'".format(patient_id)
                rows = self.db_helper.read(sql_query)
                if len(rows) == 1:
                    
                    patient = Patient()
                    patient.patient_id = rows[0][0]
                    patient.name = rows[0][1]
                    patient.phone = rows[0][2]
                    patient.email = rows[0][3]
                    patient.address = rows[0][4]
                    patient.dob = rows[0][5]
                    patient.gender = rows[0][6]
                    patient.created_on = rows[0][7]

                    patient.show()

                    name = input('Enter New Patient Name: ')
                    if len(name) != 0:
                        patient.name = name

                    phone = input('Enter New Patient Phone: ')
                    if len(phone) != 0:
                        patient.phone = phone

                    email = input('Enter New Patient Email: ')
                    if len(email) != 0:
                        patient.email = email

                    address = input('Enter New Patient Address: ')
                    if len(address) != 0:
                        patient.address = address

                    dob = input('Enter New Patient DOB (yyyy-mm-dd): ')
                    if len(dob) != 0:
                        patient.dob = dob

                    gender = input('Enter New Patient Gender: ')
                    if len(gender) != 0:
                        patient.gender = gender

                    sql_query = "update Patient set name = '{}', phone = '{}', email = '{}', address='{}', dob='{}', gender='{}', created_on='{}' where patient_id = {}".format(
                        patient.name,
                        patient.phone,
                        patient.email,
                        patient.address,
                        patient.dob,
                        patient.gender,
                        patient.created_on,
                        patient.patient_id
                    )

                    self.db_helper.write(sql_query)
                    print('[DoctorsApp] Patient Updated :)')

                else:
                    print('No Such Patient found with ID:', patient_id)


            elif choice == 3:
                
                patient_id = int(input('Enter Patient ID to Delete: '))
                sql_query = "delete from Patient where patient_id = {}".format(patient_id)
                self.db_helper.write(sql_query)

            elif choice == 4:
                sql_query = "select * from Patient"
                rows = self.db_helper.read(sql_query)
                for row in rows:
                    
                    patient = Patient()
                    patient.patient_id = row[0]
                    patient.name = row[1]
                    patient.phone = row[2]
                    patient.email = row[3]
                    patient.address = row[4]
                    patient.dob = row[5]
                    patient.gender = row[6]
                    patient.created_on = row[7]

                    # print(row)
                    patient.show()
                
            elif choice == 5:
                # Explore -> How to put unique key on a column
                phone_number = input('Enter Patient Phone Number: ')
                sql_query = "select * from Patient where phone = '{}'".format(phone_number)
                rows = self.db_helper.read(sql_query)
                for row in rows:
                    print(row)

            elif choice == 6:
                sql_query = "select * from Patient where gender = 'male'"
                rows = self.db_helper.read(sql_query)
                for row in rows:
                    print(row)

            elif choice == 7:
                sql_query = "select * from Patient where gender = 'female'"
                rows = self.db_helper.read(sql_query)
                for row in rows:
                    print(row)

            elif choice == 8:
                # HW1: to explore how to write SQL quert with sort asc, desc
                # sql_query = "select * from Patient where created_on = {}"
                sql_query = "select * from Patient"
                rows = self.db_helper.read(sql_query)
                for row in rows:
                    print(row)

            elif choice == 0:
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
            print('0: Quit')
            choice = int(input('Enter Your Choice: '))
            
            if choice == 1:
                patient_id = 0
                answer = input('Do you have patient id? (yes/no): ')
                if answer == 'yes':
                    patient_id = int(input('Enter Patient Id: '))
                else:
                    phone_number = int(input('Enter Patient Phone Number: '))
                    sql_query = "select * from Patient where phone = '{}'".format(phone_number)
                    rows = self.db_helper.read(sql_query)

                    if len(rows) == 1:
                        # rows[0][0] -> first 0 index is row, and second 0 index is patient_id
                        patient_id = rows[0][0]
                        print('Patient Found:', rows[0][1])
                    else:
                        print('sorry. no such record found with phon_number', phone_number)
                
                if patient_id != 0:

                    consultation = Consultation()
                    consultation.input_consultation_details()
                    consultation.patient_id = patient_id

                    sql_query = "insert into Consultation values(null, {}, '{}', '{}', '{}', '{}')".format(
                        consultation.patient_id,
                        consultation.remarks,
                        consultation.medicines,
                        consultation.followup,
                        consultation.created_on,
                    )

                    self.db_helper.write(sql_query)

                else:
                    print('Consultation Cannot be Created without Patient ID :)')

            elif choice == 2:
                # HW2: update consultation of a patient
                patient_id = input('Enter Patient Id to Update Details: ')
                # Before i Update, i will fetch the exiting patient details
                sql_query = "select * from Consultation where patient_id = '{}'".format(patient_id)
                rows = self.db_helper.read(sql_query)
                if len(rows) == 1:
                    
                    patient = Patient()
                    consultation.patient_id = rows[0][0]
                    consultation.remarks = rows[0][1]
                    consultation.medicines = rows[0][2]
                    consultation.followup = rows[0][3]
                    consultation.created_on = rows[0][4]

                    consultation.show()

                    remarks = input('Enter New Patient Remaks: ')
                    if len(remarks) != 0:
                        consultation.remarks = remarks

                    medicines = input('Enter New Patient Medicines: ')
                    if len( medicines ) != 0:
                        consultation.medicines =  medicines 

                    followup = input('Enter New Patient Followup: ')
                    if len(followup) != 0:
                        consultation.followup = followup

                    sql_query = "update into Consultation values(null, {}, '{}', '{}', '{}', '{}')".format(
                        consultation.patient_id,
                        consultation.remarks,
                        consultation.medicines,
                        consultation.followup,
                        consultation.created_on,
                    )


                    self.db_helper.write(sql_query)
                    print('[DoctorsApp] Consultation Updated :)')

                else:
                    print('No Such Consultation found with ID:', patient_id)



            elif choice == 3:
                consultation_id = int(input('Enter Consulation Id: '))
                sql_query = "delete from Consultation where consultation_id = {}".format(consultation_id)
                self.db_helper.write(sql_query)
            
            elif choice == 4:
                sql_query = "select * from Consultation"
                rows = self.db_helper.read(sql_query)
                for row in rows:
                    # HW3: Convert row to consultation and use show function"
                    consultation = Patient()
                    consultation.patient_id = row[0]
                    consultation.remarks = row[1]
                    consultation.medicines = row[2]
                    consultation.followup = row[3]
                    consultation.created_on = row[4]

                    # print(row)
                    consultation.show()
                
                    print(row)

            elif choice == 5:
                patient_id = int(input('Enter Patient Id: '))
                sql_query = "select * from Consultation where patient_id = {}".format(patient_id)
                rows = self.db_helper.read(sql_query)
                for row in rows:
                    print(row)
                
            elif choice == 0:
                print('~~~~~~~~~~~~~~~~~~~~~~~~')
                print('Consultation Menu Opened')
                print('~~~~~~~~~~~~~~~~~~~~~~~~')
                break
            else:
                print('Enter Suitable Menu Option...')