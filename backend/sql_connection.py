import mysql.connector
__cnx = None

def get_sql_connection():

	global __cnx

	if __cnx is None:
		__cnx = mysql.connector.connect(user='root',password='r12345678+',host='localhost',database='grocerydb')

	return __cnx