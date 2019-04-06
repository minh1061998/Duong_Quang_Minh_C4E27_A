from pymongo import MongoClient
from  bson.objectid import ObjectId

mongo_uri ="mongodb+srv://admin:admin@cluster0-iopq3.mongodb.net/test?retryWrites=true"
client = MongoClient(mongo_uri)

bike_data = client.bike_database

bike_colection = bike_data["Bike"]
