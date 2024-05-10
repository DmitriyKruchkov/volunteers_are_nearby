from flask import Flask
from flask_login import LoginManager
from redis import Redis
from config import SECRET_KEY, REDIS_HOST, REDIS_PORT
from services.users import getUserByID
from data import db_session

app = Flask(__name__, template_folder="templates")
app.config['SECRET_KEY'] = SECRET_KEY
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view("login")
login_manager.login_message = "Авторизуйтесь для доступа к закрытым страницам"
login_manager.login_message_category = "success"
redis_client = Redis(host=REDIS_HOST, port=REDIS_PORT)
login_manager.user_loader(getUserByID)
db_session.global_init("db/volunteerium.db")
