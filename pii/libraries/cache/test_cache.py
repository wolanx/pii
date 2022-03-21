import time

from pii.libraries.cache.test_localcache import funcCache
from pii.libraries.cache.redis_cache import funcRedisCache
from pii.libraries.test.unit_test import MyTestCase


@funcCache(ttl=5)
def test_func(id_):
    return 123


@funcRedisCache(ttl=5)
def test_redis(id_):
    return 123


class Test(MyTestCase):
    def test_func(self):
        print(test_func(37))
        print(test_func(2))

        print(test_func(37))
        print(test_func(2))

        time.sleep(3)

        print(test_func(37))
        print(test_func(2))

        time.sleep(3)

        print(test_func(37))
        print(test_func(2))

        print(test_func(37))
        print(test_func(2))

    def test_redis(self):
        print(test_redis(37))
        print(test_redis(2))

        print(test_redis(37))
        print(test_redis(2))

        time.sleep(3)

        print(test_redis(37))
        print(test_redis(2))

        time.sleep(3)

        print(test_redis(37))
        print(test_redis(2))

        print(test_redis(37))
        print(test_redis(2))
