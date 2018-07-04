from flask import jsonify, request, make_response
from functools import wraps
import jwt

from instance.config import Config


def token_required(f):
    """Checks for authenticated users with valid token in the header"""

    @wraps(f)
    def decorated(*args, **kwargs):
        """validate token provided"""
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if token is None:
            return make_response(jsonify({"txt": "Please Register and Login"}), 401)

        try:
            data = jwt.decode(token, Config.SECRET)
        except():
            return make_response(jsonify({"txt": "Please, provide a valid token."}), 401)
        return f(*args, **kwargs)

    return decorated


def driver_required(f):
    """Checks for authenticated driver with valid token in the header"""

    @wraps(f)
    def decorated(*args, **kwargs):
        """validate token provided and ensures the user is an admin"""

        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if token is None:
            return make_response(jsonify({"txt": "Please Register and Login"}), 401)

        try:
            data = jwt.decode(token, Config.SECRET)
            driver = data['driver']
        except():
            return make_response(jsonify({
                "txt": "Please, provide a valid token in the header"}), 401)

        if not driver:
            return make_response(jsonify({
                "txt": "You are not authorized to perform this function"}), 401)

        return f(*args, **kwargs)

    return decorated


def admin_required(f):
    """Checks for authenticated admins with valid token in the header"""

    @wraps(f)
    def decorated(*args, **kwargs):
        """validate token provided and ensures the user is an admin"""

        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if token is None:
            return make_response(jsonify({"txt": "Please Register and Login"}), 401)

        try:
            data = jwt.decode(token, Config.SECRET)
            admin = data['admin']
        except():
            return make_response(jsonify({"Please, provide a valid token in the header"}), 401)

        if not admin:
            return make_response(
                jsonify({"txt": "Sorry, You are not authorized to perform this function"}), 401)

        return f(*args, **kwargs)

    return decorated
