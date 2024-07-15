from flask import Flask
from .controller.auth_controller import auth_bp
from .extensions import init_app as init_db
from dotenv import load_dotenv
import  os

load_dotenv()
def create_app():
    app = Flask(__name__)
    SECRET_KEY = os.getenv('SECRET_KEY')
    DATABASE_URI = os.getenv('DATABASE_URL')
    print(SECRET_KEY)
    print(DATABASE_URI)
    app.config.from_object('app.config.Config')

    init_db(app)

    app.register_blueprint(auth_bp, url_prefix='/auth')

    return app
