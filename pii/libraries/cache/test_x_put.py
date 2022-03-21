import random

import time

from pii.libraries.cache.redis_cache import r
from pii.libraries.utils.time_util import TimeUtil

tName = "jdddddd"
tName = "x:topic:all"


def genObj():
    eInt = TimeUtil.nowInt()
    eName = random.choice(["qwe", "asd", "zxc"])
    eDesc = "gen in " + TimeUtil.int2str(eInt)
    b = {
        "ts": eInt,
        "eName": eName,
        "eDesc": eDesc,
        "eInt": eInt % 10,
    }
    sid = r.xadd(tName, b, maxlen=100000)
    print(sid, b)


for i in range(1, 10):
    genObj()

while True:
    genObj()
    time.sleep(0.5)
