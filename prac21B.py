import mysql

class DBHelper:
    def __init__(self, user, password, host, database):
        self.connection = mysql.connector.connect(
            user=user,
            password=password,
            host=host,
            database=database
        )
        self.cursor = self.connection.cursor()
