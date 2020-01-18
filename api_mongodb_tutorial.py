
# Examples taken from
# https://api.mongodb.com/python/current/tutorial.html
import pymongo
from pymongo import MongoClient
client = MongoClient()

# client = MongoClient('localhost', 27017)
client = MongoClient('mongodb://localhost:27017/')

db = client.test_database
# db = client['test_database']

# getting a collection
collection = db.test_collection
# collection = db['test_collection']

import datetime
post = {
    "author": "Mike",
    "text": "My first blog post",
    "tags": ["mongodb", "python", "pymongo"],
    "date": datetime.datetime.utcnow()
}

# insert a document
posts = db.posts
post_id = posts.insert_one(post).inserted_id
print('Inserted post with post_id: ', post_id)

# after first insert, we have the collection created:
print(db.list_collection_names)

# getting a single document with find_one()
import pprint
pprint.pprint(posts.find_one())

# filter to docs with author Mike:
pprint.pprint(posts.find_one( {"author": "Mike"} ))

# negative sample: filter by nonexistent value
pprint.pprint(posts.find_one( {"author": "John"} ))

# Querying by ObjectId
print("Looking for post with id = ", post_id)
pprint.pprint(posts.find_one( {"_id": post_id} ))

# a post_id is not the same as its string representation
print("post_id = ", post_id)
print("post_id as str = ", str(post_id))
print("find by str(post_id) --> ")
pprint.pprint(posts.find_one( {"_id": str(post_id)} ))

# if there is a string which is the post_id can be converted to 'real' _id by using
# from bson.objectid import ObjectId
# document_id = client.db.collection.find_one( {'_id': ObjectId(post_id)} )

# bulk inserts
new_posts = [
    {"author": "Mike",
      "text": "Another post!",
      "tags": ["bulk", "insert"],
      "date": datetime.datetime(2009, 11, 12, 11, 14)
      },
    {"author": "Eliot",
     "title": "MongoDB is fun",
     "text": "and pretty easy too!",
     "date": datetime.datetime(2009, 11, 10, 10, 45)
     }
    ]
results = posts.insert_many(new_posts)
print(results.inserted_ids)

# querying for more than one document
print('Print all posts:')
for post in posts.find():
    pprint.pprint(post)

print('Print posts by author = Mike')
for post in posts.find( {"author": "Mike"} ):
    pprint.pprint(post)

# count documents
print('Count posts:')
print(posts.count_documents)

#print('Count posts where author is Mike:')
#print(posts.count_documents( {"author": "Mike"} ) )

# range queries
print('Range queries')
d = datetime.datetime(2009, 11, 12, 12)
# for post in posts.find({"date": {"$gt": d}}).sort("author"):
for post in posts.find({"date": {"$lt": d}}).sort("author"):
    pprint.pprint(post)

# indexing
print('Indexing')
result = db.profiles.create_index([('user_id', pymongo.ASCENDING)], unique=True)
print(result)
sorted(list(db.profiles.index_information()))
print(sorted(list(db.profiles.index_information())))

user_profiles = [
    {'user_id': 211, 'name': 'Luke'},
    {'user_id': 212, 'name': 'Ziltoid'}
]
# result = db.profiles.insert_many(user_profiles)

new_profile = {'user_id': 213, 'name': 'Drew'}
duplicate_profile = {'user_id': 212, 'name': 'Tommy'}
# result = db.profiles.insert_one(new_profile)  # This is fine.
# result = db.profiles.insert_one(duplicate_profile)