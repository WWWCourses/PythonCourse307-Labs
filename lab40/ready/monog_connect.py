from pymongo import MongoClient

def connect_to_local_cluster():
  # connect using connection string:
  # 'mongodb://<username?>:<password?>@localhost:27017/<dbname?>
  connection_string = 'mongodb://localhost:27017/python_course'

  return MongoClient(connection_string)


def connect_to_atlas_cluster():
  # connect using connection string:
  # mongodb+srv://<username>:<password>@cluster0.xm0yw.mongodb.net/<dbname?>
  connection_string = 'mongodb+srv://power_user:q1a2z3@cluster0.xm0yw.mongodb.net/'

  return MongoClient(connection_string)

atlas_client = connect_to_atlas_cluster()
local_client = connect_to_local_cluster()

# list databases
print(atlas_client.list_database_names())
print(local_client.list_database_names())