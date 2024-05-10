from config import PORT, HOST, DEBUG
from core import *
from routes.users import user_router
from routes.events import events_router


app.register_blueprint(user_router)
app.register_blueprint(events_router)

if __name__ == '__main__':
    app.run(port=PORT, host=HOST, debug=DEBUG)
