from flask import Blueprint, render_template
from services.events import getActualEvents

events_router = Blueprint("news", __name__)


@events_router.route("/")
def index():
    """
        Главная страница приложения. Возвращает шаблон главной страницы.

        :return: шаблон главной страницы
        """
    actual_events = getActualEvents()
    actual_events = [elem._asdict() for elem in actual_events]
    return render_template("index.html", events=actual_events)
