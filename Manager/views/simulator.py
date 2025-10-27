from flask import Flask, request, jsonify
from ..myredis import MyRedis as Redis

class SimulatorRoutes:
    def __init__(self, app: Flask):
        self.connection = Redis()
        self.register_routes(app)


    def register_routes(self, app: Flask):
        @app.route('/simulator')
        def simulator():
            data = request.args.getlist('data')
            if len( data ) == 0:
                data = self.connection.keys();

            result = {key: 0 for key in data}
            if request.accept_mimetypes['application/json'] >= request.accept_mimetypes['text/html']:
                return jsonify(result)
            else:
                return "Happy Hamster" # TODO: Produce a table