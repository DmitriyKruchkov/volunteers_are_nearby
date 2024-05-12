from flask import Flask
from flask_login import LoginManager
from redis import Redis
from config import SECRET_KEY, REDIS_HOST, REDIS_PORT, DB_PATH
from services.users import getUserByID
import database

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
db_file = DB_PATH
conn_str = f'sqlite:///{db_file.strip()}?check_same_thread=False'
app.config['SQLALCHEMY_DATABASE_URI'] = conn_str
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
database.global_init(DB_PATH)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.user_loader(getUserByID)
#redis_client = Redis(host=REDIS_HOST, port=REDIS_PORT)
