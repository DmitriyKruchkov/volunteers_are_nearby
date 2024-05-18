import json
from datetime import datetime
from core import redis_client
from data.events import Event
from data.users import User
from database import create_session


def getActualEvents():
    current_day = datetime.now().date()
    request_to_redis = f'actual-news-{current_day.strftime("%D")}'
    if not redis_client.get(request_to_redis):
        db_sess = create_session()
        query = (db_sess.query(Event.id,
                               Event.event_name,
                               Event.date_of_start,
                               Event.picture_path)
                 .filter(Event.date_of_start > current_day)
                 .order_by(Event.date_of_start))
        executed_query = []
        for i in query.all():
            i = i._asdict()
            i['date_of_start'] = i['date_of_start'].strftime('%d.%m.%Y %H:%M')
            executed_query.append(i)
        redis_client.set(request_to_redis, json.dumps(executed_query), ex=300)
        db_sess.close()
        print(executed_query)
    else:
        executed_query = json.loads(redis_client.get(request_to_redis))
    return executed_query


def getEventByID(event_id):
    db_sess = create_session()
    request_to_redis = f'event-{event_id}'
    if not redis_client.get(request_to_redis):
        query = db_sess.query(
            Event.id,
            Event.event_name,
            Event.date_of_start,
            Event.picture_path,
            Event.address,
            Event.about,
            User.nickname
        ).join(User, Event.id_responsible_user == User.id).filter(
            Event.id == event_id
        )
        executed_query = query.first()._asdict()
        executed_query['date_of_start'] = executed_query['date_of_start'].strftime('%d.%m.%Y %H:%M')
        redis_client.set(request_to_redis, json.dumps(executed_query), ex=300)
    else:
        executed_query = json.loads(redis_client.get(request_to_redis))
    return executed_query


def getAllEvents():
    current_day = datetime.now().date()
    request_to_redis = f'all-news-{current_day.strftime("%D")}'
    if not redis_client.get(request_to_redis):
        db_sess = create_session()
        query = db_sess.query(Event.id,
            Event.event_name,
            Event.date_of_start,
            Event.picture_path,
            Event.address,
            Event.id_responsible_user
        )
        executed_query = []
        for i in query.all():
            i = i._asdict()
            i['date_of_start'] = i['date_of_start'].strftime('%d.%m.%Y %H:%M')
            executed_query.append(i)
        redis_client.set(request_to_redis, json.dumps(executed_query), ex=300)
        db_sess.close()
        print(executed_query)
    else:
        executed_query = json.loads(redis_client.get(request_to_redis))
    return executed_query
