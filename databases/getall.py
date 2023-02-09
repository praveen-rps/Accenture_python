from connectmysqldb import *

def get_all(conn):
		cursor = conn.cursor()
		sql = """ select * from employee;"""
		try:
			cursor.execute(sql)
			records = cursor.fetchall()
			print('Employee Information')
			print('--------------------')
			for record in records:
					name = record[1]+" "+record[2]
					print('Id= {}, Name = {}, Email = {}, Gender = {}, Phone = {}'
					.format(record[0],name,record[3],record[4],record[5]))
		except(Exception,Error):
			print(error)
		finally:
			if conn is not None:
				cursor.close()
				conn.close()
				print("Connections are closed")

if __name__ == '__main__':
		get_all(connect())
