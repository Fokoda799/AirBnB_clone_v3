#!/usr/bin/python3
"""Flask app module"""
from api.v1.views import app_views
from flask import Flask, jsonify
from models import storage
import os

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(exception):
    """Close any connections with storage"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """Shows not found page"""
    return jsonify({"error": "Not found"})


if __name__ == "__main__":
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', 5000))
    app.run(debug=True, host=host, port=port, threaded=True)
