#!/usr/bin/env python3
""" Flask App """
from flask import jsonify, Flask, request, Response, abort, redirect
from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route("/", methods=['GET'], strict_slashes=False)
def home():
    """ welcome message """
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=['POST'], strict_slashes=False)
def users():
    """ register users """
    email = request.form['email']
    password = request.form['password']

    try:
        user = AUTH.register_user(email, password)
    except ValueError:
        return jsonify({"message": "email already registered"}), 400
    else:
        return jsonify({"email": user.email, "message": "user created"})


@app.route("/sessions", methods=['POST'], strict_slashes=False)
def login():
    """ login users """
    email = request.form['email']
    password = request.form['password']

    if AUTH.valid_login(email, password) is False:
        abort(401)
    else:
        session_id = AUTH.create_session(email)
        response = jsonify({"email": email, "message": "logged in"})
        response.set_cookie("session_id", session_id)

    return response


@app.route("/sessions", methods=['DELETE'], strict_slashes=False)
def logout():
    """ logs user out """
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if not user:
        abort(403)
    AUTH.destroy_session(user.id)
    return redirect('/')


@app.route("/profile", methods=['GET'], strict_slashes=False)
def profile():
    """ user's profile """
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if not user:
        abort(403)
    return jsonify({"email": user.email}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
