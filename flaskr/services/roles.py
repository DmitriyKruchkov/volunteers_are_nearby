import json
from datetime import datetime

from config import REDIS_UPDATE_SECONDS
from core import redis_client
from database import create_session
from data.roles import Role


def getRole(mode_id):
    db_sess = create_session()
    # request_to_redis = f'role-id-{mode_id}'
    # if not redis_client.get(request_to_redis):
    role = db_sess.query(Role).filter(
        Role.role_id == mode_id
    ).first()
    db_sess.close()
    #     redis_client.set(request_to_redis, json.dumps(role), ex=REDIS_UPDATE_SECONDS)
    # else:
    #     role = json.loads(redis_client.get(request_to_redis))
    return role


# def getRoles():
#     db_sess = create_session()
#     current_day = datetime.now().date()
#     request_to_redis = f'roles-{current_day.strftime("%D")}'
#     if not redis_client.get(request_to_redis):
#         roles = [i._asdict() for i in db_sess.query(Role).all()]
#         db_sess.close()
#         redis_client.set(request_to_redis, json.dumps(roles), ex=300)
#     else:
#         roles = json.loads(redis_client.get(request_to_redis))
#     return roles