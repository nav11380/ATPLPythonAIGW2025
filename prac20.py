import mysql.connector as db 

class DBHelper:
    
    def __init__(self):
        self.connection = db.connect(
                        user='root',
                        password='Navdeep',
                        host='127.0.0.1',
                        database='gw2025'
                    )
        print('[DB helper] Connection created')

        self.cursor = self.connection.cursor()
        print('[DB helper] Connection created')

    def write(self, sql_query):
        print('[DB Helper] Query:', sql_query)
        self.cursor.execute(sql_query)
        self.connection.commit()
        print('[DB Helper] SQL Query Executed...')
    
    def read(self,sql_query):
        self.cursor.execute(sql_query)
        rows = self.cursor.fetchall()
        print('[DB Helper] SQL Query Executed. Rows Fetched: ', len(rows))
        return rows
    
    def close(self):
        self.connection.close()
        print('[DB Helper] DB Connection Closed...')
    

