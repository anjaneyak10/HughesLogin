from app.repository.user_repository import UserRepository
from flask_bcrypt import Bcrypt
import jwt
import datetime
from flask import current_app

bcrypt = Bcrypt()

class AuthService:

    @staticmethod
    def login(username, password):
        user = UserRepository.find_by_username(username)
        # print(check_password_hash(user['password_hash'], password))
        if user and bcrypt.check_password_hash(user['password_hash'], password):
            token = AuthService.encode_auth_token(user)
            return {'token': token}
        return None

    @staticmethod
    def register(email, name, username, role, function, password):
        if UserRepository.find_by_username(username):
            return None
        password_hash = bcrypt.generate_password_hash(password).decode('utf-8')
        user_id = UserRepository.save(email, name, username, role, function, password_hash)
        return {'id': user_id, 'username': username}

    @staticmethod
    def encode_auth_token(user):
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
                'iat': datetime.datetime.utcnow(),
                'sub': user['username'],
                'email': user['email'],
                'name': user['name'],
                'username': user['username'],
                'role': user['role'],
                'function': user['function'],
                'password_hash': user['password_hash']
            }
            user['password_hash'] = None
            return {"jwt": jwt.encode(payload, current_app.config['SECRET_KEY'], algorithm='HS256'), "user": user}
        except Exception as e:
            return e

    @staticmethod
    def get_all_users():
        users = UserRepository.get_all_users()
        return users

    @staticmethod
    def get_all_users():
        users = UserRepository.get_all_users()
        return users
