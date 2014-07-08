import datetime
import time
import sys
import  entriesdb

class Entries:
    def add_entry(self, data_entry): 
        date = datetime.date.fromtimestamp(eval(data_entry['time_in']))
        query = {'camera_id' : data_entry['camera_id'],
                 'date_in'   : str(date),
                 'item_name' : data_entry['item_name']}
        same_entry = entriesdb.find_same_entry(query)

        document = query

        if same_entry == None:
            print document
            document['count'] = 1
            entriesdb.insert_entry(document)
            
        else:
            same_entry['count'] += 1  
            entriesdb.update_entry({'_id' : same_entry['_id']},
                                     same_entry)
