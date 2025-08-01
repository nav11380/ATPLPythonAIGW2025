from flask import*
from prac24 import MongoDBHelper
from prac24A import User
import hashlib

from prac26A import Patient

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
    return render_template('home.html',name = session['name'], email = session['email'])


@web_app.route('/add-patient')
def add_patient():
    return render_template('add-patient.html',name = session['name'], email = session['email'])

# Controller
@web_app.route('/add-user', methods=['POST'])
def add_user_in_db():
    user = User()
    user.name = request.form['name']
    user.email = request.form['email']
    # encryption
    user.password = hashlib.sha256(request.form['password'].encode('utf-8')).hexdigest()
    user.show()

    result = db.insert(document=user.to_document())

    if len(str(result.inserted_id)) > 0:
        session['user_id'] = str(result.inserted_id)
        session['name'] = user.name
        session['email'] = user.email

        return render_template('home.html', name = user.name, email = user.email)
    else:
        return 'Something went wrong.Please try again'
    
@web_app.route('/add-patient-in-db', methods=['POST'])
def add_patient_in_db():
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
        return render_template('home.html', name=session['name'], email=session['email'])
    else:
        return 'Something Went Wrong. Please Try Again'


@web_app.route('/fetch-user', methods=['POST'])
def fetch_user_from_db():
    query = {
        'email': request.form['email'],
        'password': hashlib.sha256(request.form['password'].encode('utf-8')).hexdigest()
    }

    documents = db.fetch(query)

    user = documents[0]
    print(user)
    if len(documents) > 0:
        session['user_id'] = str(user['_id'])
        session['name'] = user['name']
        session['email'] = user['email']
        return render_template('home.html', name=user['name'], email=user['email'])
    else:
        return 'Username or Password Invalid. Please Try Again'

@web_app.route('/fetch-patients')
def fetch_patients_from_db():
    query = {
        'doctor_id' : session['user_id']
    }

    db.select_db(collection= 'patients')
    documents = db.fetch(query)

    user = documents[0]
    print(user)
    if len(documents) > 0:
        return render_template('patients.html', name=session['name'], 
                               email=session['email'], total=len(documents), 
                               patients=documents
                               )
    else:
        return 'Patients not Found'
   
def main():
    # Secret Key, we have to create manually of our choice
    # It is required for Session Management
    web_app.secret_key = 'doctors-app-key-v1'
    web_app.run()
    #web_app.run(port=5001)

if __name__ == '__main__':
    main()