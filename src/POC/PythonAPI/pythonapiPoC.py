import markdown
import os
from flask import Flask
from flask_restful import Resource, Api
import pymongo
from bson.json_util import dumps
import json

app = Flask(__name__)
api = Api(app)
client = pymongo.MongoClient('mongodb://192.168.1.125:27017/')
db = client["doodletestDB"]


@app.route("/")
# Display the readme when accessing index
def index():

    with open(os.path.dirname(app.instance_path) + '/README.md', 'r') as markdown_file:
        content = markdown_file.read()
        return markdown.markdown(content)


# Returns all documents in the requirement collection
class RequirementList(Resource):
    def get(self):
        docs = []
        for doc in db.requirement.find():
            docs.append(doc)

        docs = json.loads(dumps(docs))
        return docs


# Add resources
api.add_resource(RequirementList, '/requirements')

# Run and config the IP
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

