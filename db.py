from  pymongo import MongoClient
from mongopass import mongopass

client = MongoClient(mongopass)
db=client.crud
tasks_collection=db.tasks