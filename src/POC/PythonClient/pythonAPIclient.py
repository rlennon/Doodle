import requests

url = "http://192.168.1.125:5000/requirements"
response = requests.get(url)
col = response.json()
# The .json attribute has been deprecated should use the request.get_json() method.

for doc in col:
    print("Name: {}  ID: {} Width: {} Length: {} Height: {}".format(doc['name'], doc['_id']["$oid"], doc['width']
          , doc['length'], doc['height']))

from flask import Flask, request
from flask_restful import Resource, Api
#resp = request.get_json(url)
#resp1 = request
#resp1.base_url = url
#resp = resp1.get_json()
#request.url = url
#resp = request.get_json()
app = Flask(__name__)
api = Api(app)

@app.route('/requirements')

#r = requests.get('http://www.google.com')
#print(r.text)