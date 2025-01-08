import mysql.connector

connector = mysql.connector.connect(host='localhost',database='Python_db',user='root',password='')

c=connector.cursor()

Name=input("Enter Full Name:")
Mobile_no=input("Enter Mobile No.:")
Password=input("Enter Password:")
Email=input("Enter Email ID:")
Class=input("Enter Class Name:")
Rollno=input("Enter Roll No.:")

data=(Name,Mobile_no,Password,Email,Class,Rollno)

insert_query="INSERT INTO registration_form(Name,Mobile_no,Password,Email,Class,Rollno) VALUES(%s, %s, %s, %s, %s, %s)"
c.execute(insert_query,data)
connector.commit()

print("Data is added successfully!")