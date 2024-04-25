from flask import Flask, render_template, redirect
from flask_login import LoginManager, login_user, login_required, logout_user
from datetime import datetime
from data import db_session
from config import SECRET_KEY, HOST, PORT, DEBUG
from form.loginform import LoginForm
from data.users import User
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
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            # После добавления куков разкомментировать
            # login_user(user, remember=form.remember_me.data)
            login_user(user)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route("/")
def index():
    db_sess = db_session.create_session()
    current_time = datetime.now()
    query = (db_sess.query(Event.id, Event.event_name, Event.date_of_start, Event.picture_path)
             .filter(Event.date_of_start > current_time).order_by(Event.date_of_start))
    executed_query = query.all()
    events = [elem._asdict() for elem in executed_query]
    return render_template("index.html", events=events)


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter((User.email == form.email.data) | (User.nickname == form.nickname.data)).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            surname=form.name.data,
            name=form.name.data,
            nickname=form.nickname.data,
            email=form.email.data,
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
    logout_user()
    return redirect("/")


if __name__ == '__main__':
    db_session.global_init("db/volunteerium.db")
    app.run(port=PORT, host=HOST, debug=DEBUG)
