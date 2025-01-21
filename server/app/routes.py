from flask import render_template, request, jsonify
from app import app, mongo
from datetime import datetime
# import random
from app.utils import generate_random_user


@app.route("/")
def home():
    return render_template("index.html", title="Home")



@app.route("/add_user", methods=["POST"])
def add_user():

    try:
        if not request.is_json:
            return jsonify({"error": "Content-Type must be 'application/json'"}), 415
        data = generate_random_user()
        # data = request.get_json(silent=True)
        username = data.get("username")
        password = data.get("password")
        parent_email = data.get("email")


        if not username or not password:
            return jsonify({"error": "Username and password are required!"}), 400
        
        user_data = {
            "username": username,
            "email": parent_email,
            "password": password,
            "health_data": [],
            "created_at": datetime.utcnow()
        }
        mongo.cx['remote'].users.insert_one(user_data) 
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
        
            user = mongo.cx['remote'].users.find_one({"username": username})
            if not user:
                return jsonify({"error": "Invalid username or password"}), 401
        
            if user["password"] != password:
                return jsonify({"error": "Wrong Password"}), 401
        
            return jsonify({"message": f"Welcome back, {username}!", "username": username}), 200
        except Exception as e:
            return jsonify({"error": f"Failed to retrieve history: {str(e)}"}), 500

        




