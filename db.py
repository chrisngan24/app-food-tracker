import pymongo
import os

def get_connection():
    conn = pymongo.Connection(os.getenv('MONGOHQ_URL'))
    
    return conn

def test_conn():
    conn = get_connection()
    conn['test'].insert({"name":"testiiiing"})

