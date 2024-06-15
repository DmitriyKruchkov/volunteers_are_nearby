from flask import Blueprint, request, redirect
from flask_login import login_required, current_user

from services.joined_users import joinUserToEvent

join_router = Blueprint("join", __name__)


@join_router.route('/event/<int:event_id>/join')
@login_required
def join_to_event(event_id):
    """
        Функция присоединения к событию
        :return: перенаправление на страницу события
        """
    joinUserToEvent(current_user.email, event_id)
    return redirect(f'/event/{event_id}')
