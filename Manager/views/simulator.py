from flask import Flask, request, jsonify
from flask import render_template
from ..myredis import MyRedis as Redis

class SimulatorRoutes:
    def __init__(self, app: Flask):
        self.connection = Redis()
        self.register_routes(app)

    @staticmethod
    def ToString( key ):
        s = key.decode('utf-8')
        return s.split(':')[1] if ':' in s else s

    def register_routes(self, app: Flask):
        connection = self.connection

        @app.route('/simulator')
        def simulator():
            _data = request.args.getlist('data')
            _type = request.args.get('type' , 'DATA').upper()

            if not _data:
                _data = connection.keys( f"{_type}:*")

            result = {
                self.ToString(key): connection.getKey(key)
                for key in sorted(_data, key=lambda k: self.ToString(k))
            }

            if request.accept_mimetypes['application/json'] >= request.accept_mimetypes['text/html']:
                return jsonify(result)

            return render_template('redis.html', title='Simulator Data Page', data=result , type=_type )