import mysql.connector as db 

connection = db.connect(
    user = 'root',
    password = "Navdeep",
    host = '127.0.0.1',
    database = 'gu2025',
)
print('success connection created:')
print('connection',type(connection),id(connection))
cursor = connection.cursor()

sql = "select * from Vistor"
#sql = "insert into Visitor values(null, 'John', '+91 99999 11111', 'Redwood Shores', 'Fionna', 'Web Dev', '2025-07-11');"
cursor.execute(sql)
rows = cursor.fetchall()
for row in rows:
    print(row)


print("sql query executed:")

connection.close()
print('Connection Closed:')