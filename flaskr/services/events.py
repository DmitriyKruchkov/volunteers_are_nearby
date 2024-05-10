import json
from datetime import datetime
from app import redis_client
from core import db_session
from data.events import Event


def getActualEvents():
    db_sess = db_session.create_session()
    current_day = datetime.now().date()
    request_to_redis = f'news-{current_day.strftime("%D")}'
    if not redis_client.get(request_to_redis):
        query = (db_sess.query(Event.id,
                               Event.event_name,
                               Event.date_of_start,
                               Event.picture_path)
                 .filter(Event.date_of_start > current_day)
                 .order_by(Event.date_of_start))
        executed_query = query.all()
        redis_client.set(request_to_redis, json.dumps(executed_query), ex=300)
    else:
        executed_query = json.loads(redis_client.get(request_to_redis))
    return executed_query
