from config import EVENT_DATA_DIR
from data.events import Event
from services.users import download_picture
from flask_login import current_user
from database import create_session


def addSuggestedEventFromForm(form):
    db_sess = create_session()
    # Замени Event на SuggestedEvent
    suggested_event = Event(
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
