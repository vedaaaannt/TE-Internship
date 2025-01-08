import mysql.connector

connector = mysql.connector.connect(
    host='localhost',
    database='Python_db',
    user='root',
    password=''
)

c = connector.cursor()

Rollno = input("Enter the Rollno to search: ")

query = 'SELECT * FROM `registration_form` WHERE Rollno = %s'

c.execute(query,(Rollno,))

result = c.fetchall()

if result:
    for x in result:
        print(x)
else:
    print(f"No record found for Roll No.{Rollno}")

connector.close()
