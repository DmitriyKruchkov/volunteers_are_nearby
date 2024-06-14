from config import PORT, HOST, DEBUG
from routes.users import user_router
from routes.events import events_router
from routes.joined_users import join_router
from routes.suggest_event import suggest_router
from routes.manage import manage_route
from core import app

app.register_blueprint(user_router)
app.register_blueprint(events_router)
app.register_blueprint(join_router)
app.register_blueprint(suggest_router)
app.register_blueprint(manage_route)

if __name__ == '__main__':
    app.run(port=PORT, host=HOST, debug=DEBUG)
