#!/usr/bin/python3
""" The api.v1.views.states module """
from api.v1.views import app_views
from flask import jsonify, abort, make_response, request
from models import storage
from models.state import State


@app_views.route('/states', strict_slashes=False)
def all_state():
    """ A function that lists all state objects """
    all_states = storage.all(State)

    return jsonify([obj.to_dict() for obj in all_states.values()])


@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def retrieve_state(state_id):
    """ A function that retrieves a state object """
    state = storage.get(State, state_id)

    if not state:
        abort(404)

    return jsonify(state.to_dict())


@app_views.route('/states/<state_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_state(state_id):
    """ A function that deletes a state object """
    state = storage.get(State, state_id)

    if not state:
        abort(404)

    state.delete()
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def create_state():
    """ A function that creates a state object """
    new_state = request.get_json()
    if not new_state:
        abort(400, "Not a JSON")

    if "name" not in new_state:
        abort(400, "Missing name")

    state = State(**new_state)

    storage.new(state)
    storage.save()
    return make_response(jsonify(state.to_dict()), 201)


@app_views.route('/states/<state_id>',
                 methods=['PUT'], strict_slashes=False)
def update_state(state_id):
    """ A function that updates a State Object """
    state = storage.get(State, state_id)
    if not state:
        abort(404)

    body_request = request.get_json()
    if not body_request:
        abort(400, "Not a JSON")

    for k, v in body_request.items():
        if k != 'id' and k != 'created_at' and k != 'updated_at':
            setattr(state, k, v)

    storage.save()
    return make_response(jsonify(state.to_dict()), 200)
