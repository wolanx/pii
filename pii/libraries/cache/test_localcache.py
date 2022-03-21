import collections
import functools
import time
import weakref


class LocalCache:
    notFound = object()

    class Dict(dict):
        # list dict等不支持弱引用，但其子类支持，故这里包装了下
        def __del__(self):
            pass

    def __init__(self):
        self.weak = weakref.WeakValueDictionary()
        self.strong = collections.deque(maxlen=1000)

    @staticmethod
    def nowTime():
        return int(time.time())

    def get(self, key):
        value: dict = self.weak.get(key, self.notFound)
        if value is not self.notFound:
            expire = value.get("expire")
            if self.nowTime() > expire:
                return self.notFound
            else:
                return value.get("result")
        else:
            return self.notFound

    def set(self, key, val, ex):
        self.weak[key] = strongRef = LocalCache.Dict({"expire": ex, "result": val})  # strongRef作为强引用避免被回收
        self.strong.append(strongRef)  # 放入定大队列，弹出元素马上被回收


def funcCache(ttl: int = 0):
    """
    10秒内本地缓存
    @param ttl: 秒
    @return:
    """
    caches = LocalCache()

    def _wrapping(func):
        @functools.wraps(func)
        def __wrapped(*args, **kwargs):
            cacheKey = str(func) + str(args) + str(kwargs)

            res = caches.get(cacheKey)
            if res is LocalCache.notFound:
                print("==================== cache miss", func.__name__)
                res = func(*args, **kwargs)
                caches.set(cacheKey, res, ttl + caches.nowTime())
                res = caches.get(cacheKey)  # don't del
            else:
                print("==================== cache use", func.__name__)
            return res

        return __wrapped

    return _wrapping
