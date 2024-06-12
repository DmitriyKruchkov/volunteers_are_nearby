from flask import Flask
from flask_login import LoginManager
from redis import Redis
from config import SECRET_KEY, REDIS_HOST, REDIS_PORT, DB_PATH
from services.users import load_user
import database

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
database.global_init()
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.user_loader(load_user)
redis_client = Redis(host=REDIS_HOST, port=REDIS_PORT)
