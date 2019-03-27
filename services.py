from pymongo import MongoClient
from faker import Faker
from random import randint, choice
faker = Faker()

mongo_uri ="mongodb+srv://admin:admin@cluster0-iopq3.mongodb.net/test?retryWrites=true"
client = MongoClient(mongo_uri)

pilot_app = client.db_pilot

services = pilot_app["services"]

for i in range(50):
    new_services = {
        "name": faker.name(),
        "age": randint(18,30),
        "height": randint(150,190),
        "available": choice([True, False]),
        "address": faker.address(),
        "gender": choice(["male","female"]),
    }
    services.insert_one(new_services)
    print("Saving document {0}......".format(i+1))