#!/usr/bin/env python3
"""
API Authentication
"""
from flask import request
from typing import TypeVar, List


class Auth:
    """ API authentication Class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ returns False """
        return False


    def authorization_header(self, request=None) -> str:
        """ returns None """
        return None


    def current_user(self, request=None) -> TypeVar('User'):
        """ returns None """
        return None
