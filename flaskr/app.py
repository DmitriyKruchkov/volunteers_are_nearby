import os
import random
from flask import Flask, render_template, redirect
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from datetime import datetime
from werkzeug.utils import secure_filename
from data import db_session
from config import SECRET_KEY, HOST, PORT, DEBUG, DATA_DIR, NON_AVATAR_PATH
from form.loginform import LoginForm
from data.users import User
from data.roles import Role
from form.registerform import RegisterForm
from data.events import Event

app = Flask(__name__, template_folder="templates")
app.config['SECRET_KEY'] = SECRET_KEY
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/login', methods=['GET', 'POST'])
def login():
    """
        Обработка запросов на авторизацию. Проверка корректности логина и пароля.
        Если данные верны, то происходит вход в систему.

         Returns:
             html шаблон
        """
    form = LoginForm()
    if form.validate_on_submit():
        with db_session.create_session() as db_sess:
            user = db_sess.query(User).filter(User.email == form.email.data).first()
            if user and user.check_password(form.password.data):
                # После добавления куков разкомментировать
                # login_user(user, remember=form.remember_me.data)
                login_user(user)
                role = db_sess.query(Role).filter(
                    Role.role_id == current_user.mode_id
                ).first()
                current_user.logging_role = role.name
                return redirect("/")
            return render_template('login.html',
                                   message="Неправильный логин или пароль",
                                   form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route("/")
def index():
    """
        Главная страница приложения. Возвращает шаблон главной страницы.

        :return: шаблон главной страницы
        """
    db_sess = db_session.create_session()
    current_time = datetime.now()
    query = (db_sess.query(Event.id,
                           Event.event_name,
                           Event.date_of_start,
                           Event.picture_path)
             .filter(Event.date_of_start > current_time)
             .order_by(Event.date_of_start))
    executed_query = query.all()
    events = [elem._asdict() for elem in executed_query]
    return render_template("index.html", events=events)


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    """
        Регистрация нового пользователя. Валидация формы регистрации.
        Создание нового пользователя в базе данных при успешной валидации.

        :return: шаблон формы регистрации с сообщением об ошибке, если она есть
        """
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter((User.email == form.email.data) |
                                      (User.nickname == form.nickname.data)).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            surname=form.surname.data,
            name=form.name.data,
            nickname=form.nickname.data,
            email=form.email.data,
            mode_id=1,
            photo=download_picture(form.photo.data),
            about=form.about.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/logout')
@login_required
def logout():
    """
        Выход из системы. Деавторизация пользователя.

        :return: редирект на главную страницу
        """
    logout_user()
    return redirect("/")


def create_random_dir_name():
    len_of_hash = 16
    alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"
    new_dir_name = ''.join(random.sample(alphabet, len_of_hash))
    while new_dir_name in os.listdir('/'.join(['static', DATA_DIR])):
        new_dir_name = ''.join(random.sample(alphabet, len_of_hash))
    return new_dir_name


def download_picture(f):
    filename = secure_filename(f.filename)
    if filename:
        directory = create_random_dir_name()
        os.mkdir('/'.join(['./static', DATA_DIR, directory]))
        path_to_save = '/'.join([
            'static', DATA_DIR, directory, filename
        ])
        f.save(path_to_save)
        return '/'.join([DATA_DIR, directory, filename])
    return NON_AVATAR_PATH

@login_required
@app.route('/account')
@app.route("/account/info")
def account_info():
    return render_template("account_info.html")

@app.route("/account/edit")
def account_edit():
    return render_template("account_edit.html")

@app.route("/account/password")
def account_password():
    return render_template("account_password.html")




if __name__ == '__main__':
    db_session.global_init("db/volunteerium.db")
    app.run(port=PORT, host=HOST, debug=DEBUG)
