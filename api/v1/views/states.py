#!/usr/bin/python3
"""States view"""
from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.state import State


@app_views.route('/api/v1/states/<state_id>')
def states(state_id):
    """Shows states"""
    if state_id:
        states = storage.all('State')
        states_list = []
        for state in states.values():
            states_list.append(state.to_dict())
        return jsonify(states_list)
    else:
        state = storage.get('State', state_id).to_dict()
        return jsonify(state)
