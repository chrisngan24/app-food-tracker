import db

COLL_NAME = 'entries'

def find_same_entry(query):
    entry = db.find_by_match(COLL_NAME, query)
    return entry 

def insert_entry(document):
    db.insert_document(COLL_NAME, document)

def update_entry(query, document):
    db.update_document(COLL_NAME, query, document)



