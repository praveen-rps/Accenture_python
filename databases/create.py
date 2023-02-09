from connectmysqldb import *

def create_table(conn):
		cursor = conn.cursor()
		sql = """
		create table dept(deptno int, dname varchar(20), dloc varchar(20));
		"""
		try:
			cursor.execute(sql)
			conn.commit()
			print("Table created...")
		except(Exception, Error) as error:
			print(error)
		finally:
			if conn is not None:
					cursor.close()
					conn.close()
					print("Connections closed")

if __name__ == '__main__':
		create_table(connect())


	