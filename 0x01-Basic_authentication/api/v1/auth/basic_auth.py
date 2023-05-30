#!/usr/bin/env python3
""" Basic Authentication """
import re
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ Basic Auth Class """
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
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
