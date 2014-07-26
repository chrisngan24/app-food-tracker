import time 
import requests
import json


def test_add_entry(test_url):
    payload = {
            'item_name' : 'PEAR',
            'time_in'   : str(time.time()),
            'camera_id' : '012',
            'count'     : 23
            }
    r = requests.post(test_url + '/api/v1/add_entry', data=json.dumps(payload)) 

    print r
    
test_add_entry('http://localhost:8000')
