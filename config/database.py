from pymongo.mongo_client import MongoClient


client = MongoClient("mongodb+srv://<username>:<password>@npmapi.cwcmktm.mongodb.net/?retryWrites=true&w=majority&appName=<cluster>")

db = client.todo_db

collection_name = db["todo_collection"]