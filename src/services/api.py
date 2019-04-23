import markdown
import os
from flask import Flask, request, Response, jsonify
from flask_restful import Resource, Api
import pymongo
from bson.json_util import dumps
from bson import json_util, ObjectId
import json


app = Flask(__name__)
api = Api(app)

if 'DOODLE_CONFIG' in os.environ:
    filepath = os.environ['DOODLE_CONFIG']
else:
    filepath = '../config.json'

with open(filepath) as f:
    config = json.load(f)

client = pymongo.MongoClient(config.get("dbServerEndpoint"))
db = client[config.get("dbName")]


@app.route("/")
# Display the readme when accessing index
def index():

    with open(os.path.dirname(app.instance_path) + '/../README.md', 'r') as markdown_file:
        content = markdown_file.read()
        return markdown.markdown(content)


# Returns a collection of documents
class RequirementList(Resource):
    # Returns all documents in the requirement collection
    @staticmethod
    def get():
        docs = []
        for doc in db.requirement.find():
            docs.append(doc)
        resp = json.loads(dumps(docs))
        return resp


# Returns a single document or status
class Requirement(Resource):
    # Create Document
    @staticmethod
    def post():
        js = json_util.dumps(request.get_json())
        data = json_util.loads(js)
        doc = db.requirement.insert_one(data)
        resp = jsonify(json.loads(dumps(doc.inserted_id)))
        resp.status_code = 201
        return resp

    @staticmethod
    # Find document
    def get():
        doc_id = request.args.get('_Id')
        doc = db.requirement.find_one({"_id": ObjectId(doc_id)})
        resp = json.loads(dumps(doc))
        return resp

    @staticmethod
    # Delete Document
    def delete():
        doc_id = request.args.get('_Id')
        query = {"_id": ObjectId(doc_id)}
        result = db.requirement.delete_one(query)
        resp = Response()
        if result.raw_result["n"] == 0 and result.raw_result["ok"] == 1:
            resp.status_code = 404
        elif result.raw_result["ok"] == 1:
            resp.status_code = 204
        return resp

    @staticmethod
    # Update document
    def put():
        js = json_util.dumps(request.get_json())
        data = json_util.loads(js)
        doc_id = data["_id"]
        result = db.requirement.replace_one({'_id': ObjectId(doc_id)}, data)
        resp = Response()
        if result.raw_result["n"] == 0 and result.raw_result["ok"] == 1:
            resp.status_code = 404
        elif result.raw_result["ok"] == 1:
            resp.status_code = 204
        return resp


# Add resources
api.add_resource(RequirementList, '/requirements')
api.add_resource(Requirement, '/requirement')

# Run and config the IP (ip 0.0.0.0 for all IPs)
if __name__ == '__main__':
    app.run(debug=True)
