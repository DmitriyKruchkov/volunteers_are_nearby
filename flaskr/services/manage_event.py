from data.events import Event
from database import create_session
from services.users import download_picture
from config import EVENT_DATA_DIR


def loadEventsUpdates(event, form):
    db_sess = create_session()
    updated_data_to_load = {}
    attributes = ["event_name", "date_of_start", "address", "about"]
    for i in attributes:
        if getattr(form, i).data != event[i]:
            updated_data_to_load[i] = getattr(form, i).data
    if form.picture_path.data.filename:
        updated_data_to_load['picture_path'] = download_picture(form.picture_path.data, parent_dir=EVENT_DATA_DIR)
    if updated_data_to_load:
        db_sess.query(Event).filter(
            Event.id == event["id"]
        ).update(updated_data_to_load)
        db_sess.commit()
    db_sess.close()
