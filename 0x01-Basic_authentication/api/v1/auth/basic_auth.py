#!/usr/bin/env python3
""" Basic Authentication """
import re
import base64
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ Basic Auth Class """
    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """ returns Base64 part of the Authorization header
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        x = re.search("^Basic ", authorization_header)
        if not x:
            return None
        basic = re.split("^Basic ", authorization_header)
        return basic[-1]


    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """ returns the decoded value of a base64 string
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None

        try:
            value = base64_authorization_header.encode('utf-8')
            decoded_value = base64.b64decode(value)
            return decoded_value.decode('utf-8')
        except Exception:
            return None


    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """ returns the user email and password from
        the encoded string
        """
        if decoded_base64_authorization_header is None:
            return (None, None)
        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)
        x = re.search(':', decoded_base64_authorization_header)
        if not x:
            return (None, None)
        else:
            lst = re.split(':', decoded_base64_authorization_header)
            user = lst[0]
            email = lst[1]
            return (user, email)
