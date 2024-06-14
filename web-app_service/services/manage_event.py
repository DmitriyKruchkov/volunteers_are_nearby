from data.events import Event
from data.suggested_events import SuggestedEvent
from database import create_session
from services.users import download_picture
from config import EVENT_DATA_DIR


def loadEventsUpdates(event, form):
    """
        Загружается обновления для события
        """
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


def addSuggestion(suggestion_id):
    """
    Добавляет предложенную новость в  основные новости
    """
    with create_session() as db_sess:
        suggestion = db_sess.query(SuggestedEvent).filter(
            SuggestedEvent.id == suggestion_id
        ).first()
        event = Event(
            event_name=suggestion.event_name,
            id_event_type=suggestion.id_event_type,
            picture_path=suggestion.picture_path,
            date_of_start=suggestion.date_of_start,
            about=suggestion.about,
            address=suggestion.address,
            id_responsible_user=suggestion.id_responsible_user
        )
        db_sess.add(event)
        db_sess.commit()


def deleteSuggestion(suggestion_id):
    """
        Удаляет предложенную новость
    """
    with create_session() as db_sess:
        suggestion = db_sess.query(SuggestedEvent).filter(
            SuggestedEvent.id == suggestion_id
        ).first()
        db_sess.delete(suggestion)
        db_sess.commit()
