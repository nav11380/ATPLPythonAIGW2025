from prac24 import MongoDBHelper
import datetime
db = MongoDBHelper()
db.select_db()
def get_patient_by_phone(phone):
    db.select_db(collection= 'aipatients')
    documents = db.fetch(query={'phone':phone})
    if len(documents) >0:
        return documents[0]

def add_patient(name, phone, email, gender, age, symptoms):
    db.select_db(collection= 'aipatients')
    patient = get_patient_by_phone(phone)
    if patient:
        return 'Patient{} already available in the system{}.DO you wish to write a consultation'.format(name,phone)
    patient = {
        'name' : name ,
        'phone' : phone,
        'email' : email,
        'gender' : gender,
        'age' : age,
        'symptoms' : symptoms,
        'created on' : datetime.datetime.now()
        }
    result = db.insert(patient)
    if result.inserted_id:
        return'{} added to the system with phone:{}'.format(name,phone)

def save_consultation(phone, medicines, remarks):
    db.select_db(collection= 'aiconsultations')
    consultation = {
                    'phone' : phone,
                    'medicines' : medicines,
                    'remarks' : remarks
                    }
    result = db.insert(consultation)
    if result.inserted_id:
        return'consultation added for {} with medicines{}'.format(phone,medicines)