from flask import Flask
from flask import render_template
from pymongo import MongoClient
import json
from bson import json_util
from bson.json_util import dumps
import os



app = Flask(__name__)

MONGOD_HOST = 'localhost'
MONGOD_PORT = 27017
DBS_NAME = os.getenv('MONGO_DB_NAME', 'literacyUNICEF')
COLLECTION_NAME = os.getenv('MONGO_COLLECTION_NAME', 'youth')
FIELDS = {'Country': True, '_id': False, 'Year': True,
          'Total': True, 'Male': True, 'Female': True}

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/literacyUNICEF/youth")
def unicefProject():
    connection = MongoClient(MONGOD_HOST, MONGOD_PORT)
    # connection = MongoClient(MONGO_URI)
#This connection is required when hosted using a remote mongo db.
    collection = connection[DBS_NAME][COLLECTION_NAME]
    projects = collection.find(projection=FIELDS, limit=5000)
    json_projects = []
    for project in projects:
        json_projects.append(project)
    json_projects = json.dumps(json_projects, default=json_util.default)
    connection.close()
    return json_projects

if __name__ == "__main__":
    app.run(debug=True)
