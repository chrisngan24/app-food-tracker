import db

COLL_NAME = 'users'

def insert_user(document):
    db.insert_document(COLL_NAME, document)

def find_user(query):
    return db.find_by_match(COLL_NAME, query)

def update_user( user_id, user):
    db.update_document(COLL_NAME, {'user_id': user_id}, user)

