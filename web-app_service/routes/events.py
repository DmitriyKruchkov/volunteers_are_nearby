from flask import Blueprint, render_template
from services.events import getActualEvents, getEventByID

events_router = Blueprint("news", __name__)


@events_router.route("/")
def index():
    """
        Главная страница приложения. Возвращает шаблон главной страницы.

        :return: шаблон главной страницы
        """

    return render_template("index.html")


@events_router.route("/events")
def show_events():
    actual_events = getActualEvents()
    return render_template("events.html", events=actual_events)


@events_router.route('/event/<int:event_id>')
def event(event_id):
    event = getEventByID(event_id)
    return render_template("event_page.html", event=event)