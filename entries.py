import datetime
import time
import entriesdb
import util

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
            document['count'] = data_entry['count'] if data_entry.has_key('count')  else 1
            document['id'] = util.generate_uuid()
            document['time_in'] = data_entry['time_in']
            entriesdb.insert_entry(document)
        else:
            same_entry['count'] += data_entry['count'] if data_entry.has_key('count') else 1
            entriesdb.update_entry({'id' : same_entry['id']}, same_entry)

    def get_entries(self, camera_id):
        query = {
            'camera_id': camera_id,
            'count'    : { '$gt' : 0 }}        
        return entriesdb.find_entries(query)


