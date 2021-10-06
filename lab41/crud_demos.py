from pymongo import MongoClient
from pymongo.message import delete

client = MongoClient()
db = client.python_course

# res = db.todos.insert_one({"title": "Learn Django", "done": False})
# print(res.inserted_id)

# res = db.todos.insert_many([
#   {"title": "Learn Python", "done": True},
#   {"title": "Learn Flask", "done": False},
#   {"title": "Learn Flask-MongoDB", "done": False}
# ])
# print(res.inserted_ids)


# res = db.todos.insert_many([
#   {"title": "Learn Python", "done": True},
#   {"title": "Learn Flask", "description":"Learn Flask to develop quick and easy web applications with the ability to scale up."},
#   {"title": "Learn MongoDB", "due": "2021-12-31"}
# ])


# res = db.todos.find_one()
# print(res)

# find all todos: priority>1 AND completed==Flase
# for todo in db.todos.find({"$and":[
# 	{"priority":{"$gt":1}},
# 	{"completed":False}]}):
#   print(todo)

# for todo in db.todos.find({},{"title":1, "_id":0}):
# 	print(todo)

# res = db.todos.update_one({"title":"Learn PyQT"}, {"$set":{"priority":3}})



# TASK: use delete_many() to remove all documents with "completed"==True
res = db.todos.delete_many({"completed":True})
print(res)

