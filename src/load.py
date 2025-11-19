import os
from pymongo import MongoClient
from dotenv import load_dotenv
from pymongo import MongoClient


load_dotenv()

class Load:
    def load_data_atlas(self, universities, db_name: str, collection_name: str):
        client = MongoClient(os.getenv("MONGO_URI"))
        db = client[db_name]
        collection = db[collection_name]
        collection.insert_many(universities)

class Loader:
    def __init__(self, uri):
        self.client = MongoClient(uri)

    def load_data_atlas(self, universities, db_name, collection_name):
        db = self.client[db_name]
        collection = db[collection_name]
        collection.insert_many(universities)
