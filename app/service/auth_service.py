from app.repository.user_repository import UserRepository
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
from flask import current_app

class AuthService:

    @staticmethod
    def login(username, password):
        user = UserRepository.find_by_username(username)
        if user and check_password_hash(user['password_hash'], password):
            token = AuthService.encode_auth_token(user['id'])
            return {'token': token}
        return None

    @staticmethod
    def register(username, password):
        if UserRepository.find_by_username(username):
            return None
        password_hash = generate_password_hash(password)
        user_id = UserRepository.save(username, password_hash)
        return {'id': user_id, 'username': username}

    @staticmethod
    def encode_auth_token(user_id):
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
                'iat': datetime.datetime.utcnow(),
                'sub': user_id
            }
            return jwt.encode(payload, current_app.config['SECRET_KEY'], algorithm='HS256')
        except Exception as e:
            return e
