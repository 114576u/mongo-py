
import pymongo

from pymongo import MongoClient
client = MongoClient()

# client = MongoClient('localhost', 27017)
client = MongoClient('mongodb://localhost:27017')

# db = client['pymongo_test']
db = client.pymongo_test

posts = db.posts

print('Bills posts:')
bills_post = posts.find_one({'author': 'Bill'})
print(bills_post)

print('Scotts posts:')
scotts_posts = posts.find({'author': 'Scott'})
print(scotts_posts)
for p in scotts_posts:
    print(p)