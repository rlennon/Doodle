import requests
import json


url = "http://192.168.0.8:5000/"


def requirements_get():
    print("-" * 75)
    print("/requirements GET")
    url1 = url + "requirements"
    response = requests.get(url1)
    col = response.json()
    # The .json attribute has been deprecated should use the request.get_json() method.

    for doc in col:
        print("Name: {}  ID: {} Width: {} Length: {} Height: {}".format(doc['name'], doc['_id']["$oid"], doc['width']
                                                                        , doc['length'], doc['height']))


def requirement_post():
    print("-" * 75)
    print("/requirement POST")
    url1 = url + "requirement"

    payload = {
        "width": "11",
        "name": "Store Room 99",
        "length": "12",
        "height": "2"
    }
    response = requests.post(url1, json=payload)
    doc_id = json.loads(response.text)
    return doc_id["$oid"]


def requirement_get(doc_id):
    print("-" * 75)
    print("/requirement GET")
    url1 = url + "requirement"
    response = requests.get(url1, params={"_Id": doc_id})
    doc = json.loads(response.text)
    # This will print the document with the know fields
    print("Name: {}  ID: {} Width: {} Length: {} Height: {}".format(doc['name'], doc['_id']["$oid"], doc['width']
                                                                    , doc['length'], doc['height']))
    # This will print all fields in the document, sorted by key
    doc_single_line = ""
    for key, value in sorted(doc.items()):
        if key == "_id":
            doc_single_line = doc_single_line + ("ID: {}".format(value["$oid"])) + " "
        else:
            doc_single_line = doc_single_line + ("{}: {}".format(key, value)) + " "
    print(doc_single_line.rstrip())


def requirement_put(doc_id):
    print("-" * 75)
    print("/requirement PUT")
    url1 = url + "requirement"
    payload = {
        "_id": {
            "$oid": doc_id
        },
        "width": "11",
        "name": "Store Room 99",
        "length": "12",
        "height": "2",
        "new field": "Test"
    }
    requests.put(url1, json=payload)


def requirement_delete(doc_id):
    print("-" * 75)
    print("/requirement DELETE")
    url1 = url + "requirement"
    requests.put(url1, params={"_id": doc_id})


def main():
    requirements_get()
    new_id = requirement_post()
    requirement_get(new_id)
    requirement_put(new_id)
    requirement_get(new_id)
    requirement_delete(new_id)
    requirements_get()


main()


