from flask import session


class Session:
    @staticmethod
    def getSid():
        return session.sid

    @staticmethod
    def all():
        return session

    @staticmethod
    def get(name):
        if name in session:
            return session[name]
        return None

    @staticmethod
    def set(name, val):
        session[name] = val
        return True
