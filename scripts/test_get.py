import time 
import requests
import json


def test_get_inventory(test_url):
    payload = {
            'user_id' : '12345'
            }
    r = requests.get(test_url + '/api/v1/get_inventory', params=payload) 
    import pdb; pdb.set_trace()
    print r
    
test_get_inventory('http://localhost:5000')
