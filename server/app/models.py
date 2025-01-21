from flask import jsonify
from app import mongo

class User:
    @staticmethod
    def create_user(data):
        required_fields = ['username', 'email']
        
        for field in required_fields:
            if field not in data or not data[field]:
                return {"error": f"{field} is required."}
        
        if len(data['username']) < 3:
            return {"error": "Username must be at least 3 characters long."}
        
        if '@' not in data['email']:
            return {"error": "Invalid email format."}
        
        user_id = mongo.db.users.insert_one(data).inserted_id
        return {"message": "User created successfully!", "user_id": str(user_id)}
