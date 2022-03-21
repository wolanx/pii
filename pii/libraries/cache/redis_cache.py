import functools
import pickle
from datetime import datetime

import redis

from pii.libraries.mq.mq_helper import MQ_Util
from pii.libraries.utils.time_util import TimeUtil
from pii import Pii
from pii.log import log

r = redis.Redis(
    host=Pii.config.get("pii.redis.host"),
    port=int(Pii.config.get("pii.redis.port")),
    db=int(Pii.config.get("pii.redis.db")),
    password=Pii.config.get("pii.redis.password"),
)


class Redis:
    def ins(self):
        return r

    @staticmethod
    def get(name):
        b = r.get(name)
        return bytes.decode(b)


class FuncRedisCache:
    use_cache = True  # cache
    use_cache_once = True  # cache


def funcRedisCache(ttl: int = 300, eta: int = None):
    """
    10s
    @param ttl: s
    @param eta: half ttl，rebuild cache
    @return:
    """

    def _wrapping(func):
        @functools.wraps(func)
        def __wrapped(*args, **kwargs):
            funcName = func.__name__
            # fix name
            cacheKey = "func:%s.%s,%s,%s" % (func.__module__, funcName, args, kwargs)

            a = datetime.now()

            dataStr = r.get(cacheKey)
            if dataStr is None or FuncRedisCache.use_cache is False or FuncRedisCache.use_cache_once is False:
                FuncRedisCache.use_cache_once = True
                dataObj = func(*args, **kwargs)
                dataStr = pickle.dumps(dataObj)
                r.set(cacheKey, dataStr, ex=ttl)

                log.info("==================== redis %s ❌ miss %s" % (TimeUtil.msUse(a), funcName))
                return dataObj
            else:
                flush_ = round(eta if eta is not None else ttl / 2)
                ttlRedis = r.ttl(cacheKey)
                if ttlRedis < flush_:
                    MQ_Util.genFunc(func, args=args, kwargs=kwargs, in_q=True)
                    log.info(
                        "==================== redis %s ◷ %s %d=%d/%d"
                        % (TimeUtil.msUse(a), funcName, ttl, ttlRedis, flush_),
                    )
                else:
                    log.info(
                        "==================== redis %s ✔ %s %d=%d/%d"
                        % (TimeUtil.msUse(a), funcName, ttl, ttlRedis, flush_),
                    )

                #
                try:
                    dataObj = pickle.loads(dataStr)
                except Exception:
                    dataObj = func(*args, **kwargs)
                return dataObj

        return __wrapped

    return _wrapping
