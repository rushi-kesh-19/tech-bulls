
from flask import Flask
from flask_pymongo import PyMongo
from config import Config
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config["MONGO_URI"] = Config.MONGO_URI

mongo = PyMongo(app)

try:
    response = mongo.cx.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
    print("Response from MongoDB:", response)
except Exception as e:
    print(f"Failed to connect to MongoDB: {e}")


from app import routes

