from flask import Blueprint, render_template
from flask_login import login_required, current_user
from routes.account_checker import checker
from routes.events import events_router

admin_router = Blueprint("admin", __name__)



@login_required
@admin_router.route("/admin_panel")
def panel():
    return render_template("admin_panel.html")

@admin_router.route("/admin_panel/manage_users")
def manage_users():
    return