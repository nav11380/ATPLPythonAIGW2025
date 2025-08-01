# consulation,:consultaion_id,patient_id,remarks,medicines,followup,created_on
import datetime
class Consultation:
    def __init__(self, remarks = None,medicines = None,followup = None):
            self.consultation_id = 0
            self.patient_id = 0
            self.medicines = medicines
            self.followup = followup
            self.created_on = datetime.datetime.now()

    def input_consultation_details(self):
        self.remarks = input('Enter Consultation Remarks: ')
        self.medicines = input('Enter Patient Medicines: ')
        self.followup = input('Enter Patient Follow Up (yyyy-mm-dd hh:mm:ss): ')


    def show(self):
        print("~~~~~~~~~~Consulatation~~~~~~~~~~~")
        print('Consultation ID:', self.consultation_id)
        print('Patient ID:', self.patient_id)
        print('Remarks:', self.remarks)
        print('Medicines:', self.medicines)
        print('Followup:', self.followup)
        print('Craeted On:', self.created_on)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")

            