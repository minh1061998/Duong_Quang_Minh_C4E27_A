from pymongo import MongoClient
from bson.objectid import ObjectId
# Connect Mongo
mongo_uri = "mongodb+srv://admin:admin@cluster0-iopq3.mongodb.net/test?retryWrites=true"
client = MongoClient(mongo_uri)

# Get/create database
db_demo = client.test_database

# Get/create collection
first_collection = db_demo["my_collection"]

# Create document
game_document = {
    "title": "pubg",
    "description": "dead game",
}
# Insert document
# first_collection.insert_one(game_document)

# Read
# Read all
# all_document = first_collection.find()
# print(all_document)
# for document in all_document:
#     print(document["title"])

#Read one
# one_document = first_collection.find({"title":"pikachu"})
# print (one_document)

# Delete
# delete_document = first_collection.find_one({"_id": ObjectId("5c979c7396bed72c4467965f")})
# if delete_document is not None:
#     first_collection.delete_one(delete_document)
#     print("Deleted")
# else: 
#     print("Not Found")    

# Update
update_document = first_collection.find_one(({"_id": ObjectId("5c979c4196bed7040c086ac9")}))
new_value = {
    "$set":
    {
        "title":"lol"
        }
    }
first_collection.update_one(update_document,new_value)