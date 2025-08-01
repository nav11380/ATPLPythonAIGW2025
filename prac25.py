from flask import *
from prac24 import MongoDBHelper
from prac24A import User
import hashlib

web_app = Flask('Doctors App')
db = MongoDBHelper()
db.select_db(db_name= 'gw2025',collection= 'user')


@web_app.route('/') 
def index():
    return render_template('index.html')

@web_app.route('/register') 
def register():
    return render_template('register.html')

@web_app.route('/add-user',methods = ['POST'])
def add_user_in_db():
    user = User()
    user.name = request.form['name']
    user.email = request.form['email']
    user.password = hashlib.sha256 (request.form['password'].encode('utf-8')).hexdigest()
    user.show()

    db.insert(document=user.to_document())

    return render_template('home.html')

@web_app.route('/fetch-user',methods = ['POST'])
def fetch_user_from_db():
    query = {
        'email'== request.form['email'],
        'password'== hashlib.sha256(request.form['password'].encode('utf-8')).hexdigest()
    }

    documents = db.fetch(query)

    user = documents[0]
    print(user)
    
    if len(documents) >0:
        return render_template('home.html')
    else:
        return 'Username or Password is not valid.Please try again later.'

def main():
    web_app.secret_key = 'doctors-app-key-v1'
    web_app.run()

if __name__ == '__main__':
    main()