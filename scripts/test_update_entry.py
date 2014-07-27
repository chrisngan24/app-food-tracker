import time 
import requests
import json


def test_add_entry(test_url):
    item_id = 'c892698b-04b4-4150-b8e3-09560134988c'
    payload = {
            'id'  : item_id, 
            'count'     : 1
            }
    r = requests.post(test_url + '/api/v1/update_entry', params={'id': item_id},data=json.dumps(payload)) 

    print r
    
test_add_entry('http://localhost:8000')
#test_add_entry('http://shrouded-beyond-1547.herokuapp.com')
