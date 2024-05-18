from flask import Blueprint, render_template, redirect
from flask_login import login_required
from form.event_edit_form import EventEditForm
from services.manage_event import loadEventsUpdates
from services.users import privilege_mode, getUsers, addWarning, addForgiveness, userUpgrade, userDowngrade
from services.events import getAllEvents, getEventByID

manage_route = Blueprint("admin", __name__)


@manage_route.route("/manage")
@login_required
@privilege_mode
def panel():
    return render_template("manage.html")


@manage_route.route("/manage/users")
@login_required
@privilege_mode
def manage_users():
    users = getUsers()
    return render_template("manage_users.html", users=users)


@manage_route.route("/manage/users/ban/<int:user_id>")
@login_required
@privilege_mode
def ban_user(user_id):
    addWarning(user_id)
    return redirect("/manage/users")


@manage_route.route("/manage/users/unban/<int:user_id>")
@login_required
@privilege_mode
def unban_user(user_id):
    addForgiveness(user_id)
    return redirect("/manage/users")


@manage_route.route("/manage/users/upgrade/<int:user_id>")
@login_required
@privilege_mode
def upgrade_user(user_id):
    userUpgrade(user_id)
    return redirect("/manage/users")


@manage_route.route("/manage/users/downgrade/<int:user_id>")
@login_required
@privilege_mode
def downgrade_user(user_id):
    userDowngrade(user_id)
    return redirect("/manage/users")


@manage_route.route("/manage/events")
@login_required
@privilege_mode
def manage_events():
    events = getAllEvents()
    return render_template("manage_event.html", events=events)


@manage_route.route("/manage/event/<int:event_id>/edit", methods=["GET", "POST"])
@login_required
@privilege_mode
def edit_event(event_id):
    event = getEventByID(event_id)
    form = EventEditForm()
    if form.validate_on_submit():
        loadEventsUpdates(event, form)
        return redirect("/manage/events")
    form.autofill(event)
    return render_template("event_edit.html", form=form, path=event["picture_path"])


@manage_route.route("/manage/suggestions")
@login_required
@privilege_mode
def manage_suggestions():
    return
