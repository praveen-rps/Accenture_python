def get_records_count(cursor):
	cursor.execute(''' select * from dept;''')
	return len(cursor.fetchall())


def get_by_id(cursor,eid):
	query = ''' select * from employee where id = %s;'''
	cursor.execute(query, [eid])
	return cursor.fetchone();


