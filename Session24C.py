"""
    Web App Development with Flask

    1. Install Flask Library
    2. Create the Object of Flask and run it in main function
    3. Display some index content to the user

"""

from flask import *

web_app = Flask('Doctors App')

@web_app.route('/') # Decorator -> @web_app
def index():
    # Returing Text
    # return 'Welcome to My Flask Web App: Doctors App'

    html_text = """
        <html>
            <head>
                <title>Doctors App</title>
            <head>

            <body>
                <center>
                    <h1>Welcome to Flask Web App</h1>
                    <h3>Doctors App</h3>
                </center>
            </body>
        </html>
    """

    # return html_text

    return render_template('index.html')

def main():
    pass

if __name__ == '__main__':
    web_app.run()
    main()