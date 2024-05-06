from .db_session import SqlAlchemyBase
import sqlalchemy


class Role(SqlAlchemyBase):
    __tablename__ = "roles"
    role_id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String)
    connection = sqlalchemy.orm.relationship("User", back_populates="mode_connection")
