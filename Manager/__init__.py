from flask import Flask
from turbo_flask import Turbo
from .views import register_views

turbo = Turbo()

def create_app():
    app = Flask(__name__)

    turbo.init_app(app)
    app.config['SERVER_NAME'] = 'localhost:5555'  # or your actual domain
    app.config['APPLICATION_ROOT'] = '/'          # default root
    app.config['PREFERRED_URL_SCHEME'] = 'http'   # or 'https' if needed

    register_views(app)
    return app

