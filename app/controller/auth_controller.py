from flask import Blueprint, request, jsonify
from app.service.auth_service import AuthService

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    auth_token = AuthService.login(username, password)
    if auth_token:
        return jsonify({'token': auth_token}), 200
    return jsonify({'message': 'Invalid credentials'}), 401

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    user = AuthService.register(username, password)
    if user:
        return jsonify({'message': 'User created successfully'}), 201
    return jsonify({'message': 'User already exists'}), 400
