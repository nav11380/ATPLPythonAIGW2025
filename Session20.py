"""
    DataBase Helper Class
    Which will have CRUD Operations for the Objects

    1. Create Connection
    2. Create Cursor from Connection
    3. Prepare SQL Statement to be Executed
    4. Execute SQL Statement using cursor excecute() function
       OR fetchall to fecth data from database
    5. close connection to release memory resources

"""
# Controller

import mysql.connector as db

class DBHelper:
    
    def __init__(self):
        
        # 1. Create Connection
        self.connection = db.connect(
                        user='root',
                        password='',
                        host='127.0.0.1',
                        database='gw2025'
                    )
        print('[DB Helper] Connection Created...')

        # 2. Create Cursor from Connection
        self.cursor = self.connection.cursor()

        print('[DB Helper] Cursor Created...')

    # 3. Prepare SQL i.e. take sql query as input in the function
    # 4. Execute the SQL Query
    # Insert/Update/Delete Query
    def write(self, sql_query):
        self.cursor.execute(sql_query)
        print('[DB Helper] SQL Query Executed...')

    # Select Query
    def read(self, sql_query):
        self.cursor.execute(sql_query)
        rows = self.cursor.fetchall()
        print('[DB Helper] SQL Query Executed. Rows Fetched: ', len(rows))
        return rows
    
    def close(self):
        self.connection.close()
        print('[DB Helper] DB Connection Closed...')