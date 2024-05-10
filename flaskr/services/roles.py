from core import db_session
from data.roles import Role


def getRole(mode_id):
    db_sess = db_session.create_session()
    role = db_sess.query(Role).filter(
        Role.role_id == mode_id
    ).first()
    db_sess.close()