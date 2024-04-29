#!/usr/bin/python3
"""The app module to handle instantiation and
registration of blueprint"""
from api.v1.views import app_views
from flask_cors import CORS
from flask import Flask, jsonify, make_response
import os
from models import storage

app = Flask(__name__)
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/*": {"origins": '0.0.0.0'}})


@app.teardown_appcontext
def teardown(exception):
    """Close any connections with storage"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """Not found error"""
    return make_response(jsonify({"error": "Not found"}), 404)


if __name__ == "__main__":
    host = os.getenv("HBNB_API_HOST", '0.0.0.0')
    port = int(os.getenv("HBNB_API_PORT", 5000))
    app.run(debug=True, host=host, port=port, threaded=True)
