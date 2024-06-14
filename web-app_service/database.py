import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.orm import Session
from sqlalchemy import text
from sqlalchemy.exc import IntegrityError
import os

from config import DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME

SqlAlchemyBase = orm.declarative_base()

__factory = None


def global_init():
    global __factory
    if __factory:
        return
    conn_str = f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    engine = sa.create_engine(conn_str, echo=False)
    __factory = orm.sessionmaker(bind=engine)
    from data import __all_models
    SqlAlchemyBase.metadata.create_all(engine)
    session = __factory()


def create_session() -> Session:
    global __factory
    return __factory()
