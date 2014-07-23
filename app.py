import os
import flask
from flask import Flask, request, Response
import db
from entries import Entries
import json 

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/api/v1/add_entry', methods=['POST'])
def add_food_entry():
    data_entry = json.loads(request.get_data())
    
    entries = Entries()
    entries.add_entry(data_entry) 
    return 'success'

    

@app.route('/api/v1/get_inventory', methods=['GET'])
def get_inventory():
    user_id = request.args.get('user_id') 

    entries = Entries()
    inventory = entries.get_entries(user_id)

    return Response(json.dumps(inventory), mimetype='application/json')
    #return flask.jsonify(inventory)

if __name__ == '__main__':
    app.run(port=8000, debug=True)
   
