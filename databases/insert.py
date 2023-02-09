import mysql.connector


try:
	conn = mysql.connector.connect(host="localhost",user="root",passwd="root",database="accenture")

	cursor = conn.cursor()

	sql = """ insert into students(htno,name,branch) values(%s,%s,%s); """
	
	htno = input("Enter the hallticket number")
	name =input("Enter student name")
	branch=input("enter branch")

	data =[(htno,name,branch)]
	cursor.executemany(sql,data)
	conn.commit()
	print("Record Inserted....")
	
except(Exception, Error) as error:
	print(error)
