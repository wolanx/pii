import pickle
from uuid import uuid4

from flask import Flask, Request
from flask.sessions import SessionInterface, SessionMixin
from werkzeug.datastructures import CallbackDict

from pii.log import log


def total_seconds(td):
    return td.days * 60 * 60 * 24 + td.seconds


class ServerSideSession(CallbackDict, SessionMixin):
    """
    Baseclass for server-side based sessions.
    """

    def __init__(self, initial=None, sid=None):
        def on_update(self):
            self.modified = True

        CallbackDict.__init__(self, initial, on_update)
        self.sid = sid
        self.permanent = True
        self.modified = False


class MyRedisSessionInterface(SessionInterface):
    """
    @see flask session 0.4.0
    """

    serializer = pickle
    session_class = ServerSideSession

    def __init__(self, redis, keyPrefix):
        self.redis = redis
        self.keyPrefix = keyPrefix

    def open_session(self, app: "Flask", request: "Request"):
        authHead = request.headers.get("Authorization", "").split()

        sid = None
        if len(authHead) == 2:
            sid = authHead[1]
        else:
            if request.host == "localhost:6300":
                # localhost允许 cookie
                sid = request.cookies.get(app.session_cookie_name)

        if not sid:
            sid = str(uuid4())
            return self.session_class(sid=sid)

        val = self.redis.get(self.keyPrefix + sid)
        if val is None:
            return self.session_class(sid=str(uuid4()))

        try:
            data = self.serializer.loads(val)
            return self.session_class(data, sid=sid)
        except Exception as e:
            log.error(e)
            return self.session_class(sid)

    def save_session(self, app, session, response):
        if not session:
            if session.modified:
                self.redis.delete(self.keyPrefix + session.sid)
            return

        val = self.serializer.dumps(dict(session))
        self.redis.setex(
            name=self.keyPrefix + session.sid, value=val, time=total_seconds(app.permanent_session_lifetime)
        )
