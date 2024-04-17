from flask import Flask, jsonify
from flask_cors import CORS
from flask_pymongo import PyMongo
from bson.json_util import dumps
from dotenv import load_dotenv

load_dotenv()  # This loads the variables from .env

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:4200"}})

# Note: Be cautious about posting sensitive credentials like usernames and passwords in your code.
app.config["MONGO_URI"] = "mongodb+srv://Cluster03209:U1FofkxLXGlE@cluster03209.c4bojqj.mongodb.net/mongodbVSCodePlaygroundDB?retryWrites=true&w=majority"

mongo = PyMongo(app, tlsAllowInvalidCertificates=True)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/app/data')
def get_data():
    db = mongo.db
    test_collection = db.test
    test_document = test_collection.find()
    # Use bson.json_util.dumps to serialize the document directly to JSON
    return dumps(test_document), 200, {'Content-Type': 'application/json'}

@app.route('/add')
def add_user():
    mydb = mongo["test"]
    mycol = mydb["test"]
    mycol.insert_one({'name': 'John Doe', 'email': 'john@example.com'})
    return 'User added.'

@app.route('/get')
def get_user():
    user = mongo.db.users.find_one({'name': 'John Doe'})
    return f"User Found: {user['name']}"

@app.route('/update')
def update_user():
    mongo.db.users.update_one({'name': 'John Doe'}, {'$set': {'email': 'newemail@example.com'}})
    return 'Email updated.'

@app.route('/delete')
def delete_user():
    mongo.db.users.delete_one({'name': 'John Doe'})
    return 'User deleted.'

if __name__ == '__main__':
    app.run(debug=True)
