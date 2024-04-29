#!/usr/bin/python3
"""States view"""
from api.v1.views import app_views
from flask import jsonify, abort, request, make_response
from models.state import State
from models import storage


@app_views.route('/states/', strict_slashes=False)
def states():
    """ Get all of states"""
    states = storage.all('State')
    states_list = []
    for state in states.values():
        states_list.append(state.to_dict())
    return jsonify(states_list)


@app_views.route('/states/<state_id>', strict_slashes=False)
def state(state_id):
    """ Get one state """
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    return jsonify(state.to_dict())


@app_views.route('/states/<state_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_state(state_id):
    """ Delete one state """
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    storage.delete(state)
    storage.save()
    return {}


@app_views.route('/states/', methods=['POST'], strict_slashes=False)
def create_state():
    """ Create one state """
    state = request.get_json()
    if not state:
        abort(400, "Not a JSON")
    if 'name' not in state:
        abort(400, "Missing name")
    new_state = State(**state)
    storage.new(new_state)
    storage.save()
    storage.reload()
    return make_response(jsonify(new_state.to_dict()), 201)


@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def update_state(state_id):
    """ Update one state """
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    chn = request.get_json()
    if not chn:
        abort(400, "Not a JSON")
    state.name = chn['name']
    storage.save()
    return jsonify(state.to_dict())
