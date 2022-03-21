import time

import jwt


class PiiJwt:
    salt = "grundfos"

    @classmethod
    def encode(cls, payload: dict, ttl: int = None):
        if ttl:
            payload.update({"exp": int(time.time() + ttl)})
        return jwt.encode(payload=payload, key=cls.salt, algorithm="HS256")

    @classmethod
    def decode(cls, token: str):
        return jwt.decode(token, key=cls.salt, algorithms="HS256")
