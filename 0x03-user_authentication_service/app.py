#!/usr/bin/env python3
""" Flask App """
from flask import jsonify, Flask, request, Response
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
