from flask import Blueprint, request, redirect
from flask_login import login_required, current_user

from services.joined_users import joinUserToEvent

join_router = Blueprint("join", __name__)


@join_router.route('/event/<int:event_id>/join', methods=['POST', 'GET'])
@login_required
def join_to_event(event_id):
    if request.method == "POST":
        joinUserToEvent(current_user.email, event_id)
    return redirect(f'/event/{event_id}')
