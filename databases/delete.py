from connectmysqldb import *
from helper import *

def delete(conn,eid):
		cursor = conn.cursor()
		query = ''' delete from employee where id = %s;'''
		try:
				record = get_by_id(cursor,eid)
				if record is None:
						print("Employee id = {} not found".format(eid))
				else:
						cursor.execute(query,[eid])
						conn.commit()
						print("employee id = {} deleted ".format(eid))
		except(Exception, error) as error:
				print(error)
		finally:
				if conn is not None:
						cursor.close()
						conn.close()
						print("connections closed")


if __name__ == '__main__':
	n= int(input("enter id value"))
	delete(connect(),n)