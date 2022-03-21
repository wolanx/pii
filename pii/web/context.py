from flask import g

"""
AppContext，内部封装：app和g
RequestContext，内部封装：request和session
"""


class AppContext:
    @staticmethod
    def set(name: str, value):
        g.setdefault(name, value)

    @staticmethod
    def get(name: str, default=None):
        return g.get(name, default)

    @property
    def isCN(self) -> bool:
        return g.get("isCN", False)
