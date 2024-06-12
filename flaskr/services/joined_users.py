import datetime
import json

from sqlalchemy.exc import IntegrityError

from config import MAILER_HOST, MAILER_PORT
from data.events import Event
from data.joined_users import JoinedUsers
from database import create_session
import requests


def getJoinedUsers():
    db_sess = create_session()
    return db_sess.query(JoinedUsers).all()


def joinUserToEvent(email, event_id):
    db_sess = create_session()
    url = f"http://{MAILER_HOST}:{MAILER_PORT}/alert/"
    event = db_sess.query(Event).filter(Event.id == event_id).first()
    data = {
        "email": email,
        "alert_date": event.date_of_start.isoformat(),
        "message": "Вы записались на событие",
        "event_title": event.event_name,
        "event_description": event.about
    }
    requests.post(url, json.dumps(data), headers={'Content-Type': 'application/json'})
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

