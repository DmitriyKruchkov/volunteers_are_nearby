from database import create_session
from data.roles import Role


def getRole(mode_id):
    db_sess = create_session()
    role = db_sess.query(Role).filter(
        Role.role_id == mode_id
    ).first()
    db_sess.close()
    return role
