import mysql.connector
from mysql.connector import Error
from readconfig import *

def connect():
	try:
			params = read_db_params()
			conn = mysql.connector.connect(
					host = params.get('DB','host'),
					user = params.get('DB','username'),
					password = params.get('DB','password'),
					database = params.get('DB','database')
			)
			print("connected")
			return conn
	except(Exception, Error):
			print(error)