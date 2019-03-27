from pymongo import MongoClient

mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(mongo_uri)

Ex1 = client.c4e
comment = Ex1["posts"]

document = {
    "title": "Góp ý",
    "author": "Dương Quang Minh",
    "content": "Mong anh Quân chấm bài cho bọn em"
}
comment.insert_one(document)