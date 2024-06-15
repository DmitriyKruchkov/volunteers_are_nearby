import sqlalchemy

import database


# модель типов событий
class EventType(database.SqlAlchemyBase):
    __tablename__ = 'event_types'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String)

    connection = sqlalchemy.orm.relationship("Event", back_populates="event_type")
