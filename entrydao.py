import db

COLL_NAME = 'entries'

def find_same_entry(item_name, date_in):
    entry = db.find_by_match(COLL_NAME, {
        'item_name' : item_name,
        'date_in' : date_in
      })
    return entry 







