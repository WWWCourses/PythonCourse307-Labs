from pymongo import MongoClient

connection_string = 'mongodb://localhost:27017/todos'
client = MongoClient(connection_string)

print(client.list_database_names())

print(dir(client))