import pymongo
from pymongo import MongoClient
import pprint

client = MongoClient()

db = client.project

collection = db.myCollection

post_id = collection.insert_one({'_id':11,'value':''}).inserted_id

print(post_id)





