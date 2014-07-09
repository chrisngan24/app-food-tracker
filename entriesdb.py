import db

COLL_NAME = 'entries'

def find_entry(query):
    entry = db.find_by_match(COLL_NAME, query)
    return entry 

def find_entries(query):
    entries = db.find_by_query(COLL_NAME, query)
    result = []
    for entry in entries:
        result.append(entry)

    return result 

def insert_entry(document):
    db.insert_document(COLL_NAME, document)

def update_entry(query, document):
    db.update_document(COLL_NAME, query, document)



