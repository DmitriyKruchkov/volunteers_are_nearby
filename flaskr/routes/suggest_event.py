from flask import Blueprint, render_template, redirect
from form.suggested_event_form import SuggestedEventForm
from services.event_types import getEventTypes
from services.suggested_events import addSuggestedEventFromForm

suggest_router = Blueprint("suggested_events", __name__)


@suggest_router.route("/event/suggest", methods=["GET", "POST"])
def create():
    form = SuggestedEventForm()
    form.setup_select_field(getEventTypes())
    if form.validate_on_submit():
        addSuggestedEventFromForm(form)
        return redirect('/')
    return render_template('suggest_event.html', form=form)