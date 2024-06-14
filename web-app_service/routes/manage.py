from flask import Blueprint, render_template, redirect
from flask_login import login_required
from form.event_edit_form import EventEditForm
from services.manage_event import loadEventsUpdates, addSuggestion, deleteSuggestion
from services.suggested_events import getSuggestedEvents
from services.users import privilege_mode, getUsers, addWarning, addForgiveness, userUpgrade, userDowngrade
from services.events import getAllEvents, getEventByID, deleteEventByID

manage_route = Blueprint("admin", __name__)


@manage_route.route("/manage")
@login_required
@privilege_mode
def panel():
    """
    Панель управления, доступна только
     администраторам и модераторам
        """
    return render_template("manage.html")


@manage_route.route("/manage/users")
@login_required
@privilege_mode
def manage_users():
    """
    Панель управления пользователями, доступна только
     администраторам и модераторам
            """
    users = getUsers()
    return render_template("manage_users.html", users=users)


@manage_route.route("/manage/users/ban/<int:user_id>")
@login_required
@privilege_mode
def ban_user(user_id):
    """
    Блокировка пользователя, доступно только
     администраторам и модераторам
                """
    addWarning(user_id)
    return redirect("/manage/users")


@manage_route.route("/manage/users/unban/<int:user_id>")
@login_required
@privilege_mode
def unban_user(user_id):
    """
    Заблокировка пользователя, доступно только
     администраторам и модераторам
                    """
    addForgiveness(user_id)
    return redirect("/manage/users")


@manage_route.route("/manage/users/upgrade/<int:user_id>")
@login_required
@privilege_mode
def upgrade_user(user_id):
    """
    Повышение пользователя, доступно только
     администраторам и модераторам
                    """
    userUpgrade(user_id)
    return redirect("/manage/users")


@manage_route.route("/manage/users/downgrade/<int:user_id>")
@login_required
@privilege_mode
def downgrade_user(user_id):
    """
        Понижение пользователя, доступно только
         администраторам и модераторам
                        """
    userDowngrade(user_id)
    return redirect("/manage/users")


@manage_route.route("/manage/events")
@login_required
@privilege_mode
def manage_events():
    """
        Панель управления событиями, доступно только
         администраторам и модераторам
                        """
    events = getAllEvents()
    return render_template("manage_event.html", events=events)


@manage_route.route("/manage/event/<int:event_id>/edit", methods=["GET", "POST"])
@login_required
@privilege_mode
def edit_event(event_id):
    """
        Панель редактирования события, доступно только
         администраторам и модераторам
                        """
    event = getEventByID(event_id)
    form = EventEditForm()
    if form.validate_on_submit():
        loadEventsUpdates(event, form)
        return redirect("/manage/events")
    form.autofill(event)
    return render_template("event_edit.html", form=form, path=event["picture_path"], event_id=event_id)


@manage_route.route("/manage/event/<int:event_id>/delete")
@login_required
@privilege_mode
def delete_event(event_id):
    """
    Удаление события по ID
                            """
    deleteEventByID(event_id)
    return redirect("/manage/events")


@manage_route.route("/manage/suggestions")
@login_required
@privilege_mode
def manageSuggestions():
    """
    Панель управления предложенными событиями,
     доступно только
     администраторам и модераторам
                            """
    events = getSuggestedEvents()
    return render_template("manage_suggestions.html", events=events)


@manage_route.route("/manage/suggestion/<int:suggestion_id>/add")
@login_required
@privilege_mode
def addSuggestionRoute(suggestion_id):
    """
            Добавление предложенной новости к основным, доступно только
             администраторам и модераторам
                            """
    addSuggestion(suggestion_id)
    deleteSuggestion(suggestion_id)
    return redirect("/manage/suggestions")


@manage_route.route("/manage/suggestion/<int:suggestion_id>/delete")
@login_required
@privilege_mode
def deleteSuggestionRoute(suggestion_id):
    """
    Удаление предложенной новости, доступно только
     администраторам и модераторам
                                """
    deleteSuggestion(suggestion_id)
    return redirect("/manage/suggestions")
