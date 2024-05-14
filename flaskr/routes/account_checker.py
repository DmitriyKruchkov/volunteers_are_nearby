from flask_login import current_user


def checker(func):
    if current_user:
        return "qwe"
    else:
        return "zxc"