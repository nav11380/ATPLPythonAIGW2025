from flask import *
from Session25A import User
from Session24 import MongoDBHelper
import hashlib

web_app = Flask('Doctors App')
db = MongoDBHelper()
db.select_db(db_name='gw2025', collection='users')

# View
# HW:Validation of the Form: 
# https://www.w3schools.com/bootstrap5/bootstrap_form_validation.php
@web_app.route('/')
def index():
    return render_template('index.html')

# View
@web_app.route('/register')
def register():
    return render_template('register.html')

# Controller
@web_app.route('/add-user', methods=['POST'])
def add_user_in_db():
    user = User()
    user.name = request.form['name']
    user.email = request.form['email']
    # encryption
    user.password = hashlib.sha256(request.form['password'].encode('utf-8')).hexdigest()
    user.show()

    db.insert(document=user.to_document())

    return render_template('home.html')

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
        return render_template('home.html')
    else:
        return 'Username or Password Invalid. Please Try Again'
   

def main():
    # Secret Key, we have to create manually of our choice
    # It is required for Session Management
    web_app.secret_key = 'doctors-app-key-v1'
    web_app.run()
    # web_app.run(port=5001)

if __name__ == '__main__':
    main()