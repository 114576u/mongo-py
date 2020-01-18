
import pymongo

from pymongo import MongoClient
client = MongoClient()

# client = MongoClient('localhost', 27017)
client = MongoClient('mongodb://localhost:27017')

# db = client['pymongo_test']
db = client.pymongo_test

posts = db.posts
post_data = {
    'title': 'Python and MongoDB',
    'content': 'PyMongo is fun, you guys',
    'author': 'Scott'
}

# to insert a single document
result = posts.insert_one(post_data)
print('One post: {0}'.format(result.inserted_id))

# to insert several documents in a single go
post_1 = {
    'title': 'Python and MongoDB',
    'content': 'PyMongo is fun, you guys',
    'author': 'Scott'
}
post_2 = {
    'title': 'Virtual Environments',
    'content': 'Use virtual environments, you guys',
    'author': 'Scott'
}

post_3 = {
    'title': 'Learning Python',
    'content': 'Learn Python, it is easy',
    'author': 'Bill'
}

new_result = posts.insert_many([post_1, post_2, post_3])
print('Multiple posts: {0}'.format(new_result.inserted_ids))

