import os
from flask import Flask
import db

app = Flask(__name__)

@app.route('/')
def hello():
    db.test_conn()
    return 'Bye World!'
"""
@app.route('/api/v1/add_food_entry')
def add_food_entry():
"""
if __name__ == '__main__':
    app.run(debug=True)
