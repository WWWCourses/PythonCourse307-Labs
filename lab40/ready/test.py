from pymongo import MongoClient

def connect_to_local_cluster():
  # connect using connection string:
  # 'mongodb://<username?>:<password?>@localhost:27017/<dbname?>
  connection_string = 'mongodb://localhost:27017/python_course'

  return MongoClient(connection_string)


client = connect_to_local_cluster()

# list databases
print(client.list_database_names())

# use python_course db
db = client.python_course
print(db)

# list all collections
print(db.list_collection_names())

# list all documents in collection
todos = db.todos.find()
for todo in todos:
	print(todo)

# insert one record:
db.todos.insert_one({
	"title": "Learn MongoDB",
	"completed":False
})

# insert many records:
db.todos.insert_many([
	{
		"title": "Learn Django",
		"completed":False
	},
	{
		"title": "Learn Flask",
		"completed":False
	}
])

# print all:
for todo in db.todos.find():
	print(todo)

