from flask import Flask
from flask import render_template
from pymongo import MongoClient
import json
import os



app = Flask(__name__)

MONGOD_HOST = 'localhost'
MONGOD_PORT = 27017

# MONGODB_URI = os.getenv('MONGODB_URI')
DBS_NAME = os.getenv('MONGO_DB_NAME', 'literacy_Unicef')
COLLECTION_NAME = os.getenv('MONGO_COLLECTION_NAME', 'youth_C')


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/literacy_Unicef/youth_C")
def unicefProject():

    fields = {'Country': True, '_id': False, 'Year': True,
              'Total': True, 'Male': True, 'Female': True}
    with MongoClient(MONGOD_HOST, MONGOD_PORT) as conn:
        collection = conn[DBS_NAME][COLLECTION_NAME]
        projects = collection.find(projection=fields)

    return json.dumps(list(projects))

if __name__ == "__main__":
    app.run(debug=True)
