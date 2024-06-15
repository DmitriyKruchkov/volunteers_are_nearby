import sqlalchemy
import database


# модель присоединившихся пользователей
class JoinedUsers(database.SqlAlchemyBase):
    __tablename__ = 'joined_users'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    event_id = sqlalchemy.Column(sqlalchemy.Integer)
    email = sqlalchemy.Column(sqlalchemy.String, unique=True)
