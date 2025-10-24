from flask import Flask, request, jsonify
from ..myredis import MyRedis as Redis

# http://localhost:5000/simulator?data="ALTITUDE"&data="LATITUDE"

def simulator(app):

    def __init__(self):
        self.connection = Redis();

    @app.route('/simulator')
    def simulator_page(self):
        data = request.args.getlist('data')
        result = {key: 0 for key in data}
        return jsonify(result)