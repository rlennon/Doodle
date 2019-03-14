import requests

url = "http://192.168.1.125:5000/requirements"
response = requests.get(url)
col = response.json()

for doc in col:
    print("Name: {}  ID: {} Width: {} Length: {} Height: {}".format(doc['name'], doc['_id']["$oid"], doc['width']
          , doc['length'], doc['height']))