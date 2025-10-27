from flask import render_template
import threading, time
from datetime import datetime
from Manager.models.cachedata import CacheData
from Manager import turbo

def HomeRoutes(app):

    def start_background_thread():
        with app.app_context():
            threading.Thread(target=UpdateStatusTable, daemon=True).start()

    @app.route('/')
    @app.route('/home')
    def Home():
        start_background_thread()
        return render_template(
            'index.html',
            title='Home Page',
            details=CacheData( refresh=False).details,
            year=datetime.now().year,
        )

    def UpdateStatusTable():
        with app.app_context():
            while True:
                print("Update")
                time.sleep(5)  ### we should let the thread tick every 5 seconds
                turbo.push(turbo.replace(
                    render_template('main.html',
                                    title='Home Page',
                                    details=CacheData().details,
                                    year=datetime.now().year),
                    'status'
                ))
