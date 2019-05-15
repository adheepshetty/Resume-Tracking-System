from kafka import KafkaConsumer
import json
import pymongo
from pymongo import MongoClient
import pprint

client = MongoClient()

db = client.project

collection = db.myCollection

consumer = KafkaConsumer('test',
                         group_id='my-group',
                         bootstrap_servers=['localhost:9092'])


KafkaConsumer(auto_offset_reset='latest',value_deserializer=lambda m: json.loads(m.decode('ascii')))


for message in consumer:
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
    #print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,message.offset, message.key,message.value))
    try:
    	post_id = collection.insert_one(json.loads(message.value)).inserted_id
    	print(post_id)
    except pymongo.errors.DuplicateKeyError: 
    	print("-",end='')
    except:
    	print("Error")
    	break



