#!/usr/bin/python3
"""Status of my API"""
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status', strict_slashes=False)
def status():
    """ Shows http status """
    return jsonify({"status": "OK"})


@app_views.route('/stats', strict_slashes=False)
def stats():
    """ Shows number of ech class"""
    data = {
               "amenities": storage.count('Amenity'),
               "cities": storage.count('City'),
               "places": storage.count('Place'),
               "reviews": storage.count('Review'),
               "states": storage.count('State'),
               "users": storage.count('User')
           }
    view = jsonify(data)
    view.status_code = 200
    return view
