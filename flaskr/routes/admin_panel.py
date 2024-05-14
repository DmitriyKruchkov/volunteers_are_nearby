from flask import Blueprint, render_template
from flask_login import login_required, current_user
from routes.events import events_router

admin_router = Blueprint("admin", __name__)




@admin_router.route("/admin_panel")
@login_required
def panel():
    return render_template("admin_panel.html")

@admin_router.route("/admin_panel/manage_users")
@login_required
def manage_users():
    return