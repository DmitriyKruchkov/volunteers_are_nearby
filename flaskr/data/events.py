import sqlalchemy
from flask_login import UserMixin
from .db_session import SqlAlchemyBase


class Event(SqlAlchemyBase):
    __tablename__ = 'events'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    id_responsible_user = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"))
    id_event_type = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("event_types.id"))
    event_name = sqlalchemy.Column(sqlalchemy.String)
    date_of_start = sqlalchemy.Column(sqlalchemy.String)
    address = sqlalchemy.Column(sqlalchemy.String)
    about = sqlalchemy.Column(sqlalchemy.String)
    responsible_user = sqlalchemy.orm.relationship('User')
    event_type = sqlalchemy.orm.relationship('EventType')