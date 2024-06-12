import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.orm import Session
from sqlalchemy import text
from sqlalchemy.exc import IntegrityError
import os

SqlAlchemyBase = orm.declarative_base()

__factory = None


def global_init(db_file):
    global __factory

    if __factory:
        return

    if not db_file or not db_file.strip():
        raise Exception("Необходимо указать файл базы данных.")

    if not os.path.exists('db'):
        os.mkdir('db')

    conn_str = f'sqlite:///{db_file.strip()}?check_same_thread=False'
    print(f"Подключение к базе данных по адресу {conn_str}")

    engine = sa.create_engine(conn_str, echo=False)
    __factory = orm.sessionmaker(bind=engine)

    from data import __all_models

    SqlAlchemyBase.metadata.create_all(engine)

    session = __factory()

    # user = User(
    #     surname=os.getenv("SURNAME"),
    #     name=os.getenv("NAME"),
    #     nickname=os.getenv("NICKNAME"),
    #     email=os.getenv("EMAIL"),
    #     mode_id=3,
    #     photo=download_picture(""),
    #     about=os.getenv("SURNAME")
    # )
    # user.set_password(os.getenv("PASSWORD"))
    # try:
    #     session.add(user)
    #     session.commit()
    # except IntegrityError:
    #     pass

    values = [
        {"role_id": 1, "name": "Пользователь"},
        {"role_id": 2, "name": "Модератор"},
        {"role_id": 3, "name": "Администратор"}
    ]

    for value in values:
        try:
            session.execute(
                text("INSERT INTO roles (role_id, name) VALUES (:role_id, :name)"),
                value
            )
        except IntegrityError:
            continue

    values = [
        {"id": 1, "name": "Cоциальное"},
        {"id": 2, "name": "Патриотическое"},
        {"id": 3, "name": "Зооволонтерство"},
        {"id": 4, "name": "Научное"}
    ]
    for value in values:
        try:
            session.execute(
                text("INSERT INTO event_types (id, name) VALUES (:id, :name)"),
                value
            )
        except IntegrityError:
            continue
    session.commit()

    session.close()


def create_session() -> Session:
    global __factory
    return __factory()
