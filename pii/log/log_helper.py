import logging
import numbers
from json.encoder import JSONEncoder
from typing import Any

from pii import Pii

# logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

match Pii.config.get("pii.logging.level", default="info"):
    case "warn":
        _level = logging.WARN
    case "debug":
        _level = logging.DEBUG
    case _:
        _level = logging.INFO


class PiiLogger(logging.Logger):
    def __init__(self, name: str, level=logging.NOTSET) -> None:
        super().__init__(name, level)

        self.setLevel(_level)  # 觉得太多没用
        self.root.handlers.clear()

        ch = logging.StreamHandler()
        ch.setLevel(_level)
        self.formatter = PiiLoggerFormatter(
            fmt='time="%(asctime)s" type=%(name)s level=%(levelname)s caller="%(caller)s"',
            datefmt="%Y-%m-%dT%H:%M:%S%z",
        )
        ch.setFormatter(self.formatter)

        self.addHandler(ch)

    def withFields(self, ret):
        return self

    def withFormatter(self, func):
        self.formatter.setExt(func)


class PiiLoggerFormatter(logging.Formatter):
    ext: Any = None

    def format(self, record):
        if record.funcName == "<module>":
            caller = f"{record.filename}:{record.lineno}"
        else:
            caller = f"{record.module}.{record.funcName}"

        record.__setattr__("caller", caller)
        record.levelname = record.levelname.lower()
        msg = JSONEncoder().encode(str(record.msg))

        ret = super().format(record)

        if self.ext:
            mor = logfmt(self.ext())
            if mor:
                ret += " " + mor

        return f"{ret} msg={msg}"

    def setExt(self, func):
        self.ext = func


def logfmt(extra):
    outarr = []
    for k, v in extra.items():
        if v is None:
            outarr.append("%s=" % k)
            continue

        if isinstance(v, bool):
            v = "true" if v else "false"
        elif isinstance(v, numbers.Number):
            pass
        else:
            if isinstance(v, (dict, object)):
                v = str(v)
            v = '"%s"' % v.replace('"', '\\"')
        outarr.append("%s=%s" % (k, v))
    return " ".join(outarr)


PiiLogger.manager.setLoggerClass(PiiLogger)
