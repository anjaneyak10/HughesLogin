from flask import Flask
from .controller.auth_controller import auth_bp
from .extensions import db

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    db.init_app(app)

    app.register_blueprint(auth_bp, url_prefix='/auth')

    return app
