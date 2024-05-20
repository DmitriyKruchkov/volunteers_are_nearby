import os
import random
from functools import wraps
from flask import abort
from flask_login import current_user
from werkzeug.utils import secure_filename
from config import USER_DATA_DIR, NON_AVATAR_PATH
from data.users import User
from database import create_session


def getUserByEmail(email):
    db_sess = create_session()
    return db_sess.query(User).filter(User.email == email).first()


def getUserByID(user_id):
    db_sess = create_session()
    return db_sess.query(User).get(user_id)


def load_user(user_id):
    db_sess = create_session()
    user = db_sess.query(User).get(user_id)
    if user and user.warnings_count < 2:
        return user


def privilege_mode(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if current_user.mode_id not in [2, 3]:
            abort(403)  # Запретить доступ пользователям без роли администратора
        return func(*args, **kwargs)

    return wrapper


def checkUsers(email, nickname):
    db_sess = create_session()
    query = db_sess.query(User).filter((User.email == email) |
                                       (User.nickname == nickname)).first()
    if query:
        return True
    return False


def addUserFromForm(form):
    db_sess = create_session()
    user = User(
        surname=form.surname.data,
        name=form.name.data,
        nickname=form.nickname.data,
        email=form.email.data,
        mode_id=1,
        photo=download_picture(form.picture_path.data),
        about=form.about.data
    )
    user.set_password(form.password.data)
    db_sess.add(user)
    db_sess.commit()
    db_sess.close()


def download_picture(f, parent_dir=USER_DATA_DIR):
    filename = secure_filename(f.filename)
    if filename:
        if not os.path.exists(os.path.join('static', parent_dir)):
            os.mkdir(os.path.join('static', parent_dir))
        directory = create_random_dir_name(parent_dir)
        os.mkdir(os.path.join('static', parent_dir, directory))
        path_to_save = os.path.join(
            'static', parent_dir, directory, filename
        )
        f.save(path_to_save)
        return os.path.join(parent_dir, directory, filename)
    return NON_AVATAR_PATH


def create_random_dir_name(parent_dir):
    len_of_hash = 16
    alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"
    new_dir_name = ''.join(random.sample(alphabet, len_of_hash))
    while new_dir_name in os.listdir(os.path.join('static', parent_dir)):
        new_dir_name = ''.join(random.sample(alphabet, len_of_hash))
    return new_dir_name


def loadNewData(form):
    db_sess = create_session()
    updated_data_to_load = {}
    for i in set(vars(form)) & set(vars(current_user)) ^ {"photo"}:
        if getattr(current_user, i) != (getattr(form, i)).data:
            updated_data_to_load[i] = (getattr(form, i)).data
    if form.photo.data.filename:
        updated_data_to_load['photo'] = download_picture(form.photo.data)
    if updated_data_to_load:
        db_sess.query(User).filter(
            User.id == current_user.id
        ).update(
            updated_data_to_load
        )
        db_sess.commit()
    db_sess.close()


def changePassword(form):
    db_sess = create_session()
    user = db_sess.query(User).filter(User.id == current_user.id).first()
    if user.check_password(form.old_password.data):
        user.set_password(form.new_password.data)
        db_sess.query(User).filter(User.id == current_user.id).update({User.hashed_password: user.hashed_password})
        db_sess.commit()
        db_sess.close()
        return True
    return False


def getUsers():
    db_sess = create_session()
    users = db_sess.query(User).filter(User.mode_id < current_user.mode_id).all()
    db_sess.close()
    return users


def addWarning(user_id):
    db_sess = create_session()
    user = db_sess.query(User).filter(
        User.id == user_id
    )
    executed = user.first()
    if executed:
        if executed.warnings_count < 2:
            if executed.mode_id not in [3, current_user.mode_id]:
                user.update(
                    {User.warnings_count: User.warnings_count + 1}
                )
                db_sess.commit()
    db_sess.close()


def addForgiveness(user_id):
    db_sess = create_session()
    user = db_sess.query(User).filter(
        User.id == user_id
    )
    executed = user.first()
    if executed:
        if executed.warnings_count > 0:
            if executed.mode_id not in [3, current_user.mode_id]:
                user.update(
                    {User.warnings_count: User.warnings_count - 1}
                )
                db_sess.commit()
    db_sess.close()


def userUpgrade(user_id):
    db_sess = create_session()
    user = db_sess.query(User).filter(
        User.id == user_id
    )
    executed = user.first()
    if executed:
        if executed.mode_id == 1:
            if executed.mode_id not in [3, current_user.mode_id]:
                user.update(
                    {User.mode_id: 2}
                )
                db_sess.commit()
    db_sess.close()


def userDowngrade(user_id):
    db_sess = create_session()
    user = db_sess.query(User).filter(
        User.id == user_id
    )
    executed = user.first()
    if executed:
        if executed.mode_id == 2:
            if executed.mode_id not in [3, current_user.mode_id]:
                user.update(
                    {User.mode_id: 1}
                )
                db_sess.commit()
    db_sess.close()
