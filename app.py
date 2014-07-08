import os
from flask import Flask, request
import db
from entry import Entry
import json 

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Bye World!'

@app.route('/api/v1/add_entry', methods=['POST'])
def add_food_entry():
    data_entry = json.loads(request.get_data())
    
    entry = Entry()
    entry.add_entry(data_entry) 
    return 'success'


if __name__ == '__main__':
    app.run(debug=True)
    
