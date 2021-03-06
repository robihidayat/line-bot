# from flask import jsonify
from pymongo import MongoClient
import os

class BaseMongo:

    def __init__(self):
        self.client = MongoClient(os.getenv('MONGODB_URI', 'mongodb://localhost:27017/linebot'),
                     connectTimeoutMS=30000,
                     socketTimeoutMS=None,
                     socketKeepAlive=True)
        self.db = self.client.get_default_database()
