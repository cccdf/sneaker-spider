import pymongo
import json

client = pymongo.MongoClient(
    "mongodb+srv://root:jmvjII4YHyVpFzZa@cluster0-tkywk.mongodb.net/test?retryWrites=true&w=majority")
db = client.root
collection = db.snkrs
with open('snkrsUpcoming.json') as f:
    file_data = json.load(f)
    # file_data = json.dumps(data)
print(type(file_data))
x = collection.delete_many({})
print(x.deleted_count, "documents deleted")
y = collection.insert_many(file_data)
print(len(y.inserted_ids), "doucuments inserted")

collectionReleased = db.nikes
with open('sneaker.json') as f:
    released = json.load(f)
    # file_data = json.dumps(data)
print(type(released))
x1 = collectionReleased.delete_many({})
print(x1.deleted_count, "documents deleted")
y1 = collectionReleased.insert_many(released)
print(len(y1.inserted_ids), "doucuments inserted")
client.close()
