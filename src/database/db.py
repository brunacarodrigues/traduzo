from pymongo import MongoClient
import os

mongo_uri = os.environ.get('MONGO_URI', 'mongodb://localhost:27017')
db_name = os.environ.get('DB_NAME', 'test_db_traduzo')
client = MongoClient(mongo_uri)
db = client[db_name]
