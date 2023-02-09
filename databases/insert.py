import mysql.connector
from mysql.connector import Error

try:
	conn = mysql.connector.connect(host="localhost",user="root",passwd="root",database="accenture")

	cursor = conn.cursor()

	sql = """ insert into employee(id,first_name,last_name,email,gender,phone) values(%s,%s,%s,%s,%s,%s); """
	
	data =[(10,'sai','gopal','saigopal@gmail.com','m','123-456-7890'),(11,'krishna','govind','krg@gmail.com','m','999-888-6666')]
	cursor.executemany(sql,data)
	conn.commit()
	print("Record(s) Inserted....")
	
except(Exception, Error) as error:
	print(error)
