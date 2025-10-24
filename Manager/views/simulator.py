from flask import Flask, request, jsonify

# http://localhost:5000/simulator?data="ALTITUDE"&data="LATITUDE"

def simulator(app):
    @app.route('/simulator')
    def simulator_page():
        data = request.args.getlist('data')
        result = {key: 0 for key in data}
        return jsonify(result)