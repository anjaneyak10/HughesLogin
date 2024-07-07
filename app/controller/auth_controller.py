from flask import Blueprint, request, jsonify
from app.service.auth_service import AuthService
from flask_cors import cross_origin

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/login', methods=['POST'])
@cross_origin()
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    auth_details = AuthService.login(username, password)
    if auth_details:
        return jsonify(auth_details), 200
    return jsonify({'message': 'Invalid credentials'}), 401

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    name = data.get('name')
    username = data.get('username')
    role = data.get('role')
    function = data.get('function')
    password = data.get('password')
    user = AuthService.register(email, name, username, role, function, password)
    if user:
        return jsonify({'message': 'User created successfully'}), 201
    return jsonify({'message': 'User already exists'}), 400

@auth_bp.route('/getallusers', methods=['GET'])
@cross_origin()
def get_all_users():
    users = AuthService.get_all_users()
    if users:
        return jsonify(users), 200
    return jsonify({'message': 'No users found'}), 404
