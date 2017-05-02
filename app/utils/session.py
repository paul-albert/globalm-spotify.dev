# User session's utility

from flask import session


class Session(object):

    def get(self, key):
        try:
            return session[key]
        except KeyError:
            return None

    def set(self, key, value, default_value):
        try:
            session[key] = value
        except KeyError:
            session[key] = default_value
