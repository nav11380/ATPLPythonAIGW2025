"""
    >>Virtual Environment
    An env where we have python, pip and 
    other library packages (which we install)
    which we can use in our project

    >> How to create it ?
    python -m venv myenv
    OR
    python3 -m venv myenv

    >> How to activate it ?
    (windows)
    .\myenv\Scripts\activate

    (mac/linux)
    source myenv/bin/activate

    >> Install the MySQL Connector
    pip install mysql-connector-python

    >> List all packages installed in Virtual Env
    pip list

    >> Generate a requirements.txt file 
    pip freeze > requirements.txt

    >> Once, your project is done
    if you go to some other system. you need not to install every single library 
    pip install -r requirements.txt

"""

# Hence, we have successfully integrated mysql connector in our project
import mysql.connector as db

# 1. Create Connection
connection  = db.connect(
    user='root',
    password='',
    host='127.0.0.1',
    database='gw2025'
)

print('Conenction Created :)')
print(connection, type(connection), id(connection))

# 2. Obtain Cursor from Conenction
cursor = connection.cursor()

# 3. Execute SQL Statement
# 3.1 Command to be execute from Python Program
# sql = "insert into Visitor values(null, 'Harry', '+91 99999 22222', 'Redwood Shores', 'Fionna', 'Web Dev', '2025-07-14')"
# sql = "update Visitor set name='John Watson', address='Country Homes' where serial_no = 2;"
# sql = "delete from Visitor where serial_no = 3"

sql = "select * from Visitor"

# 3.2 Execute the SQL Statement
# cursor.execute(sql)

# 3.3 Commit the Transaction
# connection.commit()

cursor.execute(sql)
rows = cursor.fetchall()
for row in rows:
    print(row)

print('SQL Query Executed :)')

# 4. Close connection -> Released the memory resources
connection.close()
print('Connection Closed :)')
