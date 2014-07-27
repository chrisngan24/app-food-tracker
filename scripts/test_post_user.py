import time 
import requests
import json


def test_add_entry(test_url):
    user_id = '012'
    payload = {
            'user_id'   : user_id,
            'camera_id' : user_id,
            'grocery_list': ['ORANGE', 'RED APPLE', 'SALMON', 'HAMBURGER']
            }
    r = requests.post(test_url + '/api/v1/update_user', params={'user_id': user_id }, data=json.dumps(payload)) 

    print r
    
test_add_entry('http://localhost:8000')
