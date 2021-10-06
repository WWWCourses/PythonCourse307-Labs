import pymongo
from datetime import datetime

client = pymongo.MongoClient()
db = client.python_course
print(db)

res = db.todos.insert_many([
	{
		"title": "Learn Python",
		"completed": True,
		"dueDate": datetime.fromisoformat("2021-07-01"),
		"priority": 1
	},
	{
		"title": "Learn Flask",
		"description":"Learn Flask to develop quick and easy web applications with the ability to scale up.",
		"completed": True,
		"dueDate": datetime.fromisoformat("2022-01-12"),
		"priority": 2
	},
	{
		"title": "Learn MongoDB",
		"completed": False,
		"dueDate": datetime.fromisoformat("2022-01-12"),
		"priority": 1
	},
	{
		"title": "Learn PyQT",
		"completed": False,
		"dueDate": datetime.fromisoformat("2021-12-01"),
		"priority": 2
	}
])

print(res.inserted_ids)