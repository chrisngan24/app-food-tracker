import datetime
import time
import entriesdb

class Entries:
    def add_entry(self, data_entry): 
        date = datetime.date.fromtimestamp(eval(data_entry['time_in']))
        query = {'camera_id' : data_entry['camera_id'],
                 'date_in'   : str(date),
                 'item_name' : data_entry['item_name']}
        same_entry = entriesdb.find_entry(query)

        document = query

        if same_entry == None:
            print document
            document['count'] = 1
            entriesdb.insert_entry(document)
            
        else:
            same_entry['count'] += 1  
            entriesdb.update_entry({'_id' : same_entry['_id']}, same_entry)

    def get_entries(self, camera_id):
        query = {
            'camera_id': camera_id,
            'count'    : { '$gt' : 0 }}        
        return entriesdb.find_entries(query)


