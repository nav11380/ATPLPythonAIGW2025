from flask import *

web_app = Flask('Doctors App')

@web_app.route('/')
def index():
    return render_template('index.html')

@web_app.route('/register')
def register():
    return render_template('register.html')

def main():
    # Secret Key, we have to create manually of our choice
    # It is required for Session Management
    web_app.secret_key = 'doctors-app-key-v1'
    web_app.run()

if __name__ == '__main__':
    main()