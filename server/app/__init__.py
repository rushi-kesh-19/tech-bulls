
from flask import Flask
from flask_pymongo import PyMongo
from config import Config
from flask_cors import CORS

import cloudinary
import cloudinary.uploader
import cloudinary.api

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


try:
    cloudinary.config(
        cloud_name=Config.CLOUDINARY_CLOUD_NAME,
        api_key=Config.CLOUDINARY_API_KEY,
        api_secret=Config.CLOUDINARY_API_SECRET
    )
    print("Successfully connected to Cloudinary!")
except Exception as e:
    print(f"Failed to connect to Cloudinary: {e}")



from app import routes

