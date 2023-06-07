#!/usr/bin/env python3
""" Authentication """
import bcrypt
from db import DB
from sqlalchemy.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """ takes in a password string
    arg and returns bytes
    """
    byte = password.encode('utf-8')

    salt = bcrypt.gensalt()

    return (bcrypt.hashpw(byte, salt))


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> object:
        """ registers a new user """
        try:
            find_user = self._db.find_user_by(email=email)
        except NoResultFound:
            hashed_password = str(_hash_password(password))
            new_user = self._db.add_user(email, hashed_password)

            return new_user

        raise ValueError(f"User {email} already exists")
