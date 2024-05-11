from flask import Blueprint, render_template, redirect, request, flash
from flask_login import current_user, login_required

from services.events import getActualEvents, getEventByID
from services.joined_users import joinUserToEvent


events_router = Blueprint("news", __name__)


@events_router.route("/")
@events_router.route("/events")
def index():
    """
        Главная страница приложения. Возвращает шаблон главной страницы.

        :return: шаблон главной страницы
        """
    actual_events = getActualEvents()
    return render_template("index.html", events=actual_events)


@events_router.route('/event/<int:event_id>')
def event(event_id):
    event = getEventByID(event_id)
    return render_template("event_page.html", event=event)

@events_router.route('/event/<int:event_id>/join', methods=['POST', 'GET'])
@login_required
def join_to_event(event_id):
    if request.method == "POST":
        joinUserToEvent(current_user.email, event_id)
    return redirect(f'/event/{event_id}')
