from pymongo import MongoClient

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
all_document = first_collection.find()
print(all_document)
for document in all_document:
    print(document["title"])

#Read one
# one_document = first_collection.find({"title":"pikachu"})
# print (one_document)