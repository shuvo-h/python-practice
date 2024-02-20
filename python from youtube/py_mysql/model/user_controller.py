from flask import Blueprint, jsonify, request
from .user_model import create_user, get_all_users, get_user

user_bp = Blueprint('user_bp', __name__)

@user_bp.route("/users/user", methods=['POST'])
def add_user():
    data = request.json
    newUser = create_user(data['name'], data['email'], data['role'])
    return jsonify({'message': 'User created successfully',"newUser":newUser}), 201

@user_bp.route("/users", methods=['GET'])
def fetch_users():
    users = get_all_users()
    return jsonify(users)

@user_bp.route("/users/user/<int:user_id>", methods=['GET'])
def fetch_user(user_id):
    user = get_user(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(user)
