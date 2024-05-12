import sqlalchemy
import database


class Role(database.SqlAlchemyBase):
    __tablename__ = "roles"
    role_id = sqlalchemy.Column(sqlalchemy.Integer,
                                primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String, unique=True)
    connection = sqlalchemy.orm.relationship("User", back_populates="mode_connection")
