import os
from random import random
from flask_login import current_user
from werkzeug.utils import secure_filename
from config import DATA_DIR, NON_AVATAR_PATH
from core import db_session
from data.users import User


def getUserByEmail(email):
    db_sess = db_session.create_session()
    return db_sess.query(User).filter(User.email == email).first()


def getUserByID(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


def checkUsers(email, nickname):
    db_sess = db_session.create_session()
    query = db_sess.query(User).filter((User.email == email) |
                                       (User.nickname == nickname)).first()
    if query:
        return True
    return False


def addUserFromForm(form):
    db_sess = db_session.create_session()
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
    db_sess.close()


def download_picture(f):
    filename = secure_filename(f.filename)
    if filename:
        directory = create_random_dir_name()
        os.mkdir(os.path.join('static', DATA_DIR, directory))
        path_to_save = os.path.join(
            'static', DATA_DIR, directory, filename
        )
        f.save(path_to_save)
        return os.path.join(DATA_DIR, directory, filename)
    return NON_AVATAR_PATH


def create_random_dir_name():
    len_of_hash = 16
    alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"
    new_dir_name = ''.join(random.sample(alphabet, len_of_hash))
    while new_dir_name in os.listdir(os.path.join('static', DATA_DIR)):
        new_dir_name = ''.join(random.sample(alphabet, len_of_hash))
    return new_dir_name


def loadNewData(form):
    db_sess = db_session.create_session()
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
    db_sess = db_session.create_session()
    user = db_sess.query(User).filter(User.id == current_user.id).first()
    if user.check_password(form.old_password.data):
        user.set_password(form.new_password.data)
        db_sess.query(User).filter(User.id == current_user.id).update({User.hashed_password: user.hashed_password})
        db_sess.commit()
        db_sess.close()
        return True
    return False
