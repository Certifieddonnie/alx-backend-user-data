#!/usr/bin/env python3
""" Authentication """
import bcrypt


def _hash_password(password: str) -> bytes:
    """ takes in a password string
    arg and returns bytes
    """
    byte = password.encode('utf-8')

    salt = bcrypt.gensalt()

    return (bcrypt.hashpw(byte, salt))
