from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import database
import sqlalchemy


class User(database.SqlAlchemyBase, UserMixin):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    surname = sqlalchemy.Column(sqlalchemy.String)
    name = sqlalchemy.Column(sqlalchemy.String)
    nickname = sqlalchemy.Column(sqlalchemy.String)
    about = sqlalchemy.Column(sqlalchemy.String)
    email = sqlalchemy.Column(sqlalchemy.String,
                              index=True, unique=True)
    photo = sqlalchemy.Column(sqlalchemy.String)
    mode_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('roles.role_id'), nullable=True)
    mode_connection = sqlalchemy.orm.relationship('Role')
    hashed_password = sqlalchemy.Column(sqlalchemy.String)
    logging_role = ''

    def __repr__(self):
        return ' '.join([self.name, self.email, self.nickname])

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)
