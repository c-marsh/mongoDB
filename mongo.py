import pymongo
import os

MONGO_URI = os.environ['MONGO_URI']
DBS_NAME = "myFirstMDB"
COLLECTION_NAME = "myFirstMDB"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to Mongo: %s") % e


conn = mongo_connect(MONGO_URI)

coll = conn[DBS_NAME][COLLECTION_NAME]

new_doc = {'first': 'douglas', 'last': 'adams', 'dob': '11/03/1952',
           'hair_colour': 'grey', 'occupation': 'author', 'nationality': 'english'}

coll.insert(new_doc)

documents = coll.find()

for doc in documents:
    print(doc)
