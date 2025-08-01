from flask import *
import patient
from prac24 import MongoDBHelper
from prac24A import User
from prac26A import Patient
from prac29A import Consultation
from bson.objectid import ObjectId

import hashlib


web_app = Flask('Doctors App')
db = MongoDBHelper()
db.select_db(db_name='gw2025', collection='users')

@web_app.route('/')
def index():
    return render_template('index.html')

# View
@web_app.route('/register')
def register():
    return render_template('register.html')

@web_app.route('/home')
def home():
    if len(session['user_id']) > 0:
        return render_template('home.html',name = session['name'], email = session['email'])
    else:
        return redirect('/')

@web_app.route('/add-patient')
def add_patient():
    if len(session['user_id']) > 0:
        return render_template('add-patient.html',name = session['name'], email = session['email'])
    else: 
        return redirect('/')
    
@web_app.route('/add-consultation/<id>')
def add_consultation(id):
    
    query ={'_id':ObjectId(id)}
    db.select_db(collection= 'patients')
    patient = db.fetch(query)[0]

    session['patient_id'] = id
    session['patient_name'] = patient['name']

    if len(session['user_id']) > 0:
        return render_template('add-consultation.html',name = session['name'], email = session['email'],patient_name= patient['name'])
    else: 
        return redirect('/')
    
    
@web_app.route('/logout')
def logout():
    
    session['user_id'] = ''
    session['name'] =  ''
    session['email'] =''
    return redirect('/')

@web_app.route('/search-patient', methods=['POST'])
def search_patient_in_db():
    patient_id = request.form.get('patient_id')
    results = db.search('patients', {'id': patient_id})
    if not results:
        return render_template('patient_not_found.html'), 404
    return render_template('patient_results.html', patients=results)


@web_app.route('/search-patient', methods=['POST'])
def search_patient_in_db():
    search = request.form['search']
    query ={
        '$or':[
            {'name': {'$regex': search, '$options': 'i'}},
            {'phone': {'$regex': search, '$options': 'i'}},
            {'email': {'$regex': search, '$options': 'i'}},
        ],
        'doctor_id': session['user_id']
    }
    
    db.select_db(collection='patients')
    documents = db.fetch(query)

    if len(documents) == 1:
        return render_template('patient-card.html', name=session['name'], 
                                email=session['email'], 
                                patient=documents[0]
                                )
    elif len(documents) > 1:
        return render_template('patients.html', name=session['name'], 
                                email=session['email'], total=len(documents), 
                                patients=documents
                                )
    else:
       return render_template('error.html', message='No Patient Found for the search {}'.format(search), name=session['name'], email=session['email'])
   

# Controller
@web_app.route('/add-user', methods=['POST'])
def add_user_in_db():
    
    user = User()
    user.name = request.form['name']
    user.email = request.form['email']
    # encryption
    user.password = hashlib.sha256(request.form['password'].encode('utf-8')).hexdigest()
    user.show()

    db.select_db(collection='users')
    result = db.insert(document=user.to_document())

    if len(str(result.inserted_id)) > 0:
        session['user_id'] = str(result.inserted_id)
        session['name'] = user.name
        session['email'] = user.email

        return render_template('home.html', name = user.name, email = user.email)
    else:
        return render_template('error.html', message = 'Something went wrong.Please try again',name = session['name'], email = session['email'])
    
@web_app.route('/add-patient-in-db', methods=['POST'])
def add_patient_in_db():
    
    if len(session['user_id'])> 0:

        patient = Patient()
        patient.name = request.form['name']
        patient.phone = request.form['phone']
        patient.email = request.form['email']
        patient.address = request.form['address']
        patient.gender = request.form['gender']
        patient.age = request.form['age']
        patient.doctor_id = session['user_id']
    
        print(patient.to_document())

        db.select_db(collection='patients')
        result = db.insert(document=patient.to_document())

        if len(str(result.inserted_id)) > 0:
            return render_template('success.html', message = 'Patient{} added successfully in the system'.format(patient.name), name=session['name'], email=session['email'])
        else:
            return render_template('error.html', message='Something Went Wrong. Try Again', name=session['name'], email=session['email'])
    
    else:
        return redirect('/')
    
@web_app.route('/add-consultation-in-db', methods=['POST'])
def add_consultation_in_db():

    if len(session['user_id']) > 0:

        consultation = Consultation()
        consultation.patient_name = session['patient_name'] 
        consultation.weight = request.form['weight']
        consultation.fever = request.form['fever']
        consultation.bphigh = request.form['bphigh']
        consultation.bplow = request.form['bplow']
        consultation.sugar = request.form['sugar']
        consultation.complaints = request.form['complaints']
        consultation.medicines = request.form['medicines']
        consultation.followup = request.form['followup']
        consultation.patient_id = session['patient_id'] # Patient ID
        consultation.doctor_id = session['user_id'] # Doctor ID
    
        print(consultation.to_document())

        db.select_db(collection='consultations')
        result = db.insert(document=consultation.to_document())

        if len(str(result.inserted_id)) > 0:
            return render_template('success.html', message='Consultation with medicines {} added successfully in the system'.format(consultation.medicines), name=session['name'], email=session['email'])
        else:
            return render_template('error.html', message='Something Went Wrong. Try Again', name=session['name'], email=session['email'])
    
    else:
        return redirect('/')

    
@web_app.route('/fetch-user', methods=['POST'])
def fetch_user_from_db():
    query = {
        'email': request.form['email'],
        'password': hashlib.sha256(request.form['password'].encode('utf-8')).hexdigest()
    }

    db.select_db(collection='users')
    documents = db.fetch(query)
  
    user = documents[0]
    #print(user)
    if len(documents) > 0:
        session['user_id'] = str(user['_id'])
        session['name'] = user['name']
        session['email'] = user['email']
        return render_template('home.html', name=user['name'], email=user['email'])
    else:
        return render_template('error.html', message='Username or Password Invalid. Please Try Again', name=session['name'], email=session['email'])
   

@web_app.route('/fetch-patients')
def fetch_patients_from_db():
    if len(session['user_id']) >0:
        
        query = {
            'doctor_id' : session['user_id']
        }

        db.select_db(collection= 'patients')
        documents = db.fetch(query)

        
        if len(documents) > 0:
            return render_template('patients.html', name=session['name'], 
                                email=session['email'], total=len(documents), 
                                patients=documents
                                )
        else:
            return  render_template('error.html', message='Patients Not Found', name=session['name'], email=session['email'])
    else:
        return redirect('/')
    
@web_app.route('/fetch-consultations')
def fetch_consulations_from_db():

    if len(session['user_id']) > 0:

        query = {
            'doctor_id': session['user_id']
        }

        db.select_db(collection='consultations')
        # List of Documents/Dictionaries having Patients Data
        documents = db.fetch(query) 

        if len(documents) > 0:
            return render_template('consultations.html', name=session['name'], 
                                email=session['email'], total=len(documents), 
                                consultations=documents
                                )
        else:
            return render_template('error.html', message='Consultations Not Found', name=session['name'], email=session['email'])
    else:
        return redirect('/')
    

@web_app.route('/fetch-consultations-of-patient/<id>')
def fetch_consultations_of_patient_from_db(id):

    if len(session['user_id']) > 0:

        query = {
            'doctor_id': session['user_id'],
            'patient_id': id
        }

        db.select_db(collection='consultations')
        # List of Documents/Dictionaries having Patients Data
        documents = db.fetch(query) 

        if len(documents) > 0:
            return render_template('consultations.html', name=session['name'], 
                                email=session['email'], total=len(documents), 
                                consultations=documents
                                )
        else:
            return render_template('error.html', message='Consulations Not Found', name=session['name'], email=session['email'])
    else:
        return redirect('/')
    
@web_app.route ('/delete_patient/<id>') 
def delete_patient(id):
    db.select_db(collection='patients')
    query = {'_id': ObjectId(id)}
    result =db.delete(query)
    if result.deleted_count > 0 :
        return render_template('success.html',message = 'Patient Deleted Succcessfully', name=session['name'], email=session['email'])
    else:
        return render_template('error.html',message = 'Patient Deletion Failed.Try Again',name = session['name'],email = session['email'])

@web_app.route ('/update_patient/<id>') 
def update_patient(id):
    session['patient_id'] = id

    db.select_db(collection='patients')    
    query = {'_id': ObjectId(id)}
    documents = db.fetch(query)
    if len(documents) > 0:
        patient_document = documents[0]
        return render_template('update-patient.html', 
                               name=session['name'], 
                               email=session['email'],
                               patient=patient_document)
    else:
        return render_template('error.html', message='Patient Not Found. Somethiwng Went Wrong. Try Again', name=session['name'], email=session['email'])

@web_app.route('/update-patient-in-db', methods=['POST'])
def update_patient_in_db():

    if len(session['user_id']) > 0:

        patient = Patient()
        patient.name = request.form['name']
        patient.phone = request.form['phone']
        patient.email = request.form['email']
        patient.address = request.form['address']
        patient.gender = request.form['gender']
        patient.age = request.form['age']
        patient.doctor_id = session['user_id'] # Doctor ID
    
        print(patient.to_document())

        db.select_db(collection='patients')
        query = {'_id': ObjectId(session['patient_id'])}

        result = db.update(query, patient.to_document())

        if len(str(result.modified_count)) > 0:
            return render_template('success.html', message='Patient {} Updated successfully in the system'.format(patient.name), name=session['name'], email=session['email'])
        else:
            return render_template('error.html', message='Something Went Wrong. Try Again', name=session['name'], email=session['email'])
    
    else:
        return redirect('/')

@web_app.route('/patient-details/<id>')
def patient_details(id):
    db.select_db(collection='patients')
    query = {'_id': ObjectId(id)}
    documents = db.fetch(query)
    if len(documents) > 0:
        # pass patient as an input to patient-card.html and ensure it is 0th index of documents list
        return render_template('patient-card.html', name=session['name'], email=session['email'], patient=documents[0])
    else:
        return render_template('error.html', message='Patient Details Failed. Try Again', name=session['name'], email=session['email'])

   
def main():
    # Secret Key, we have to create manually of our choice
    # It is required for Session Management
    web_app.secret_key = 'doctors-app-key-v1'
    web_app.run()
    #web_app.run(port=5001)

if __name__ == '__main__':
    main()