from pymongo import MongoClient

CONNECTION_STRING = mongodb://localhost:27017/

client = MongoClient(CONNECTION_STRING)