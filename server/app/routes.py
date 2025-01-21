from flask import render_template, request, jsonify, redirect
from app import app, mongo
from app.utils import generate_random_user
from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
import os
import cloudinary.uploader
import validators


SECRET_KEY = os.getenv("SECRET_KEY", "your_secret_key")

@app.route("/")
def home():
    return render_template("index.html", title="Home")



@app.route("/add_user", methods=["POST"])
def add_user():

    try:
        if not request.is_json:
            return jsonify({"error": "Content-Type must be 'application/json'"}), 415
        data = generate_random_user()
        data = request.get_json(silent=True)
        username = data.get("username")
        password = data.get("password")
        email = data.get("email")

        hashed_password = generate_password_hash(password)


        if not username or not email or not password:
            return jsonify({"error": "Username, password and email are required!"}), 400
        
        user_data = {
            "username": username,
            "email": email,
            "password": hashed_password
        }
        mongo.cx['hack2hire'].users.insert_one(user_data) 
        return jsonify({"message": "User added successfully!"})
    

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500



@app.route("/login", methods=["POST"])
def login():
    try:
        if not request.is_json:
            return jsonify({"error": "Content-Type must be 'application/json'"}), 415

        data = request.get_json(silent=True)
        if data is None:
            return jsonify({"error": "Invalid or empty JSON payload"}), 400

        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            return jsonify({"error": "Username and password are required!"}), 400

        print("Just before user")
        user = mongo.cx['hack2hire']['users'].find_one({"username": username})

        print(user)
        if not user:
            return jsonify({"error": "Invalid username or password"}), 401
        if not check_password_hash(user["password"], password):
            return jsonify({"error": "Wrong password"}), 401
        token = jwt.encode({
            "user_id": str(user["_id"]),
            "username": username,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }, SECRET_KEY, algorithm="HS256")

        return jsonify({"message": f"Welcome back, {username}!", "token": token}), 200

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


# @app.route("/upload", methods=["POST"])
# def upload():
#     try:
#         if 'file' not in request.files:
#             return jsonify({"error": "No file part in the request"}), 400
#         file = request.files['file']

#         if file.filename == '':
#             return jsonify({"error": "No file selected for uploading"}), 400

#         if file.content_type != 'application/pdf':
#             return jsonify({"error": "Only PDF files are allowed"}), 400

#         result = cloudinary.uploader.upload(file, resource_type="auto")

#         return jsonify({
#             "message": "File uploaded successfully",
#             "url": result.get("secure_url")
#         }), 200

#     except Exception as e:
#         return jsonify({"error": f"An error occurred: {str(e)}"}), 500


@app.route("/upload", methods=["POST"])
def upload():
    try:
        if 'file' not in request.files:
            return jsonify({"error": "No file part in the request"}), 400

        file = request.files['file']
        if file.filename == '':
            return jsonify({"error": "No file selected for uploading"}), 400

        allowed_types = ['text/csv', 'application/pdf', 
                         'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet']
        allowed_extensions = ['.csv', '.pdf', '.xlsx']
        
        if not (file.content_type in allowed_types or file.filename.endswith(tuple(allowed_extensions))):
            return jsonify({"error": "Only CSV, PDF, and XLSX files are allowed"}), 400

        result = cloudinary.uploader.upload(file, resource_type="auto")
        file_url = result.get("secure_url")
        download_url = f"{file_url}?fl_attachment={file.filename}"

        return jsonify({
            "message": "File uploaded successfully",
            "download_url": download_url
        }), 200

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500
