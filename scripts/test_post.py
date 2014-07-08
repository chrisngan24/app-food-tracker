import datetime
import requests
import json


def test_add_entry(test_url):
    payload = {
            'item_name' : 'apple',
            'date_in'   : str(datetime.datetime.utcnow())
            }
    r = requests.post(test_url + '/api/v1/add_entry', data=json.dumps(payload)) 
    print r
    
test_add_entry('http://localhost:5000')
