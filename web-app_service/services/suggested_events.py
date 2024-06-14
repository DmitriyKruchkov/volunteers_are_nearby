from config import EVENT_DATA_DIR
from data.suggested_events import SuggestedEvent
from services.users import download_picture
from flask_login import current_user
from database import create_session


def addSuggestedEventFromForm(form):
    """
        Добавляет предложенную новость из формы в предложку
        """
    db_sess = create_session()
    suggested_event = SuggestedEvent(
        id_event_type=form.id_event_type.data,
        id_responsible_user=current_user.id,
        event_name=form.event_name.data,
        date_of_start=form.date_of_start.data,
        address=form.address.data,
        about=form.about.data,
        picture_path=download_picture(form.picture_path.data, EVENT_DATA_DIR)
    )
    db_sess.add(suggested_event)
    db_sess.commit()
    db_sess.close()


def getSuggestedEvents():
    """
    Returns: Все предложенные новости
    """
    with create_session() as db_sess:
        return db_sess.query(SuggestedEvent).all()
