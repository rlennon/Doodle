"""Doodle API"""
import os
import json
import markdown
import pymongo
from flask import Flask, request, Response, jsonify
from flask_restful import Resource, Api
from bson.json_util import dumps
from bson import json_util, ObjectId


app = Flask(__name__)
api = Api(app)

if 'DOODLE_CONFIG' in os.environ:
    file_path = os.environ['DOODLE_CONFIG']

elif os.path.isfile('../config.json'):
    file_path = '../config.json'

else:
    file_path = 'config.json'

with open(file_path) as f:
    config = json.load(f)

client = pymongo.MongoClient(config.get("dbServerEndpoint"))
db = client[config.get("dbName")]


@app.route("/")
# Display the readme when accessing index
def index():
    """Displays API Readme"""
    with open(os.path.dirname(app.instance_path) + '/README.md', 'r') as markdown_file:
        content = markdown_file.read()
        return markdown.markdown(content)


def db_find():
    """Returns all Documents in the requirement collection"""
    docs = []
    try:
        for doc in db.requirement.find():
            docs.append(doc)

    except pymongo.errors.ConnectionFailure as error:
        return {str(error)}, 500

    return docs, 200


def db_find_one(doc_id):
    """Returns single document from ID"""
    try:
        doc = db.requirement.find_one({"_id": ObjectId(doc_id)})

    except pymongo.errors.ConnectionFailure as error:
        return {str(error)}, 500

    return doc, 200


def session_find_one(session_id):
    """"Checks Session by id"""
    try:
        doc = db.login.find_one({"_id": ObjectId(session_id)})

    except pymongo.errors.ConnectionFailure as error:
        return {str(error)}, 500

    return doc, 200


def db_insert_one(data):
    """Inserts document into requirement collection"""
    try:
        doc = db.requirement.insert_one(data)
        doc_id = doc.inserted_id
    except pymongo.errors.ConnectionFailure as error:
        return {str(error)}, 500

    return doc_id, 201


def db_delete_one(doc_id):
    """Deletes single document in collection"""
    try:
        result = db.requirement.delete_one({"_id": ObjectId(doc_id)})

    except pymongo.errors.ConnectionFailure as error:
        return {str(error)}, 500

    if result.raw_result["n"] == 0 and result.raw_result["ok"] == 1:
        return "Not Found", 404
    if result.raw_result["ok"] == 1:
        return "OK", 204
    return "Error", 500


def session_delete_one(doc_id):
    """Deletes single document in collection"""
    try:
        result = db.login.delete_one({"_id": ObjectId(doc_id)})

    except pymongo.errors.ConnectionFailure as error:
        return {str(error)}, 500

    if result.raw_result["n"] == 0 and result.raw_result["ok"] == 1:
        return "Not Found", 404
    if result.raw_result["ok"] == 1:
        return "OK", 204
    return "Error", 500


def db_replace_one(doc_id, data):
    """Updates single document"""
    status_code = 500
    try:
        doc = db.requirement.replace_one({'_id': ObjectId(doc_id)}, data).raw_result
        if doc["n"] == 0 and doc["ok"] == 1:
            status_code = 404
        elif doc["ok"] == 1:
            status_code = 204

    except pymongo.errors.ConnectionFailure as error:
        return {str(error)}, 500

    return doc, status_code


def session_insert_one(data):
    """Inserts document into session collection"""
    try:
        doc = db.login.insert_one(data)
        doc_id = doc.inserted_id
    except pymongo.errors.ConnectionFailure as error:
        return {str(error)}, 500

    return doc_id, 201


class RequirementList(Resource):
    """Requirement End point"""
    @staticmethod
    def get():
        """Returns all documents in the requirement collection"""
        docs, status = db_find()
        resp = Response(dumps(docs), mimetype='application/json')
        resp.status_code = status
        return resp


class Requirement(Resource):
    """Returns a single document, status, update and delete"""
    @staticmethod
    def post():
        """Create Document"""
        data = json_util.loads(json_util.dumps(request.get_json()))
        doc_id, status = db_insert_one(data)
        resp = jsonify(json.loads(dumps(doc_id)))
        resp.status_code = status
        return resp

    @staticmethod
    def get():
        """Find document"""
        doc_id = request.args.get('_Id')
        doc, status = db_find_one(doc_id)
        resp = Response(dumps(doc), mimetype='application/json')
        resp.status_code = status
        return resp

    @staticmethod
    def delete():
        """Delete Document"""
        doc_id = request.args.get('_Id')
        resp, status = db_delete_one(doc_id)
        resp = Response(dumps(resp), mimetype='application/json')
        resp.status_code = status
        return resp

    @staticmethod
    def put():
        """Update document"""
        data = json_util.loads(json_util.dumps(request.get_json()))
        doc_id = data["_id"]
        resp, status = db_replace_one(doc_id, data)
        resp = Response(dumps(resp), mimetype='application/json')
        resp.status_code = status
        return resp


class Session(Resource):
    """Create and Check session"""
    @staticmethod
    def post():
        """Create Session"""
        data = json_util.loads(json_util.dumps(request.get_json()))
        doc_id, status = session_insert_one(data)
        resp = jsonify(json.loads(dumps(doc_id)))
        resp.status_code = status
        print(doc_id)
        return resp

    @staticmethod
    def delete():
        """Delete Document"""
        doc_id = request.args.get('_Id')
        resp, status = session_delete_one(doc_id)
        resp = Response(dumps(resp), mimetype='application/json')
        resp.status_code = status
        return resp

    @staticmethod
    def get():
        """Find Session"""
        doc_id = request.args.get('_Id')
        doc, status = session_find_one(doc_id)
        resp = Response(dumps(doc), mimetype='application/json')
        resp.status_code = status
        return resp


# Add resources
api.add_resource(RequirementList, '/requirements')
api.add_resource(Requirement, '/requirement')
api.add_resource(Session, '/session')

# Run and config the IP (ip 0.0.0.0 for all IPs)
if __name__ == '__main__':
    app.run(debug=True)
