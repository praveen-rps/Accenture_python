import mysql.connector


try:
	conn = mysql.connector.connect(host="localhost",user="root",passwd="root",database="accenture")

	if conn:
			print("connection established")
	
except(Exception, Error) as error:
	print(error)

