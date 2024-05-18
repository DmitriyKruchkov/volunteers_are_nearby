from sqlalchemy.exc import IntegrityError
from data.joined_users import JoinedUsers
from database import create_session


def getJoinedUsers():
    db_sess = create_session()
    return db_sess.query(JoinedUsers).all()


def joinUserToEvent(email, event_id):
    db_sess = create_session()
    user = JoinedUsers(
        email=email,
        event_id=event_id
    )
    try:
        db_sess.add(user)
        db_sess.commit()
    except IntegrityError:
        pass
    db_sess.close()
