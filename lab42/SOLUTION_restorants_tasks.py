import pymongo

# ----------------------------------- TASK ----------------------------------- #
# Connect to your Atlas Cluster's "sample_restaurants" database.
# print only the names of the first 5 restaurants with "Japanese" cuisine in borough "Manhattan"
# Note: you can use the limit method on find cursor (db.collection.find(<query>).limit(<number>)
client = pymongo.MongoClient("mongodb+srv://admin:1234@cluster0.i4qjs.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.sample_restaurants

res = db.restaurants.find({"$and":[{"cuisine":"Japanese"},{"borough":"Manhattan"}]}).limit(10)
for r in res:
	print(r["name"], r["borough"])


# ----------------------------- EXPECTED RESULTS: ---------------------------- #
# Dan Tempura
# Hasaki Restaurant
# Souen Restaurant
# Restuarant Nippon
# Tokubei 86
# Hatsuhana Restaurant
# Tomoe Sushi
# Nada-Sushi
# Shabu-Shabu 70 Restaurant
# Omen Japanese Cuisine


