import mysql.connector


try:
	conn = mysql.connector.connect(host="localhost",user="root",passwd="root",database="accenture")

	cursor = conn.cursor()
	sql = """ create table students(htno varchar(10), name varchar(20), 
             branch varchar(20)) """
	cursor.execute(sql)
	print("Table created....")
	
except(Exception, Error) as error:
	print(error)
