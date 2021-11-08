import mysql.connector
from mysql.connector import connection

def make_connection(user, password, db, host="localhost", port=3306):
  try:
    cnx = mysql.connector.connect(
      user=user,
      password=password,
      db=db,
      host=host,
      port=port
    )

  except mysql.connector.Error as e:
    print(e)

  print('Connection Established')
  return cnx

if __name__ == '__main__':
	cnx = make_connection('root', '1234', 'test')
	print(cnx)
