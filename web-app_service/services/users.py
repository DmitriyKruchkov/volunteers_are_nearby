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
    """

    Args:
        email: почта пользователя

    Returns: Пользователь с такой почтой

    """
    db_sess = create_session()
    return db_sess.query(User).filter(User.email == email).first()


def getUserByID(user_id):
    """

    Args:
        user_id: айди пользователя

    Returns: Пользователь с таким айди

    """
    db_sess = create_session()
    return db_sess.query(User).get(user_id)


def load_user(user_id):
    """
    Функция авторизации пользователя, блокируется если 2>= предупреждений от администрации
    Args:
        user_id: айди пользователя

    Returns: Разрешенный пользователь

    """
    db_sess = create_session()
    user = db_sess.query(User).get(user_id)
    if user and user.warnings_count < 2:
        return user


def privilege_mode(func):
    '''

    Args:
        func: функция выдачи шаблона страницы

    Returns: Декоратор для страницы, которая недоступна обычным пользователям

    '''
    @wraps(func)
    def wrapper(*args, **kwargs):
        if current_user.mode_id not in [2, 3]:
            abort(403)  # Запретить доступ пользователям без роли администратора
        return func(*args, **kwargs)

    return wrapper


def checkUsers(email, nickname):
    '''

    Args:
        email:
        nickname:

    Returns: True/False - в зависимости от наличия пользователя в БД

    '''
    db_sess = create_session()
    query = db_sess.query(User).filter((User.email == email) |
                                       (User.nickname == nickname)).first()
    if query:
        return True
    return False


def addUserFromForm(form):
    '''
    Добавляет нового пользователя в БД,
     если не указана аватарка, то будет использована дефолтная
    Args:
        form: форма с сайта


    '''
    db_sess = create_session()
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


def download_picture(f, parent_dir=USER_DATA_DIR):
    '''
    Функция сохранения аватарки события/пользователя
    Args:
        f: файл
        parent_dir: родительская папка для изображения

    Returns: Путь до сохраненной картинки

    '''
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
    '''

    Args:
        parent_dir: родительская папка

    Returns: несуществующее рандомное название директории
    '''
    len_of_hash = 16
    alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"
    new_dir_name = ''.join(random.sample(alphabet, len_of_hash))
    while new_dir_name in os.listdir(os.path.join('static', parent_dir)):
        new_dir_name = ''.join(random.sample(alphabet, len_of_hash))
    return new_dir_name


def loadNewData(form):
    '''
    Просматривает все обновленные значения и обновляет их в таблице
    Args:
        form: форма для обновления данных
    '''
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
    '''
    Запись нового пароля пользователя в зашифрованном виде
    Args:
        form: форма для смены пароля
    '''
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
    '''
    Получение списка для панели управления пользователями. Выдает всех пользователей, чья роль меньше чем роль
    управляющего (для модераторов только пользователи, для администраторов: пользователи и модераторы)
    '''

    db_sess = create_session()
    users = db_sess.query(User).filter(User.mode_id < current_user.mode_id).all()
    db_sess.close()
    return users


def addWarning(user_id):
    '''

    Добавляет предупреждение пользователю

    '''
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
    '''

        Убирает предупреждение пользователю

        '''
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
    '''
        Добавляет права модератора пользователю
        '''
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
    '''
           Отбирает права модератора у пользователя
           '''
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
