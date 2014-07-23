import pymongo
import os

DB_NAME = 'python_inc'

def get_connection():
    print os.getenv('MONGOHQ_URL')
    conn = pymongo.Connection(os.getenv('MONGOHQ_URL'))
    
    return conn

def get_database():
    conn = get_connection()
    return conn[DB_NAME]

def get_collection(coll_name):
    db = get_database()
    return db[coll_name]

def test_conn():
    coll = get_collection('test')
    coll.insert({"name":"testiiiing"})

def insert_document(coll_name, document):
    coll = get_collection(coll_name)
    coll.insert(document)

def find_by_match(coll_name, query):
    coll = get_collection(coll_name) 
    return coll.find_one(query)

def find_by_query(coll_name, query, projection={}):
    coll = get_collection(coll_name) 
    return coll.find(query, projection)
    

def update_document(coll_name, query, document):
    coll = get_collection(coll_name)
    coll.update(query, document)
