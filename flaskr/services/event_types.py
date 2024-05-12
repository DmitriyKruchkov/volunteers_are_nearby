import json
from datetime import datetime

from core import redis_client
from database import create_session
from data.event_types import EventType


def getEventTypes():
    current_day = datetime.now().date()
    request_to_redis = f'event-types-{current_day}'
    if not redis_client.get(request_to_redis):
        db_sess = create_session()
        query = db_sess.query(EventType).all()
        db_sess.close()
        types = []
        for i in query:
            i = i.__dict__
            types.append((i["id"], i["name"]))
        redis_client.set(request_to_redis, json.dumps(types), ex=300)
    else:
         types = json.loads(redis_client.get(request_to_redis))
    return types