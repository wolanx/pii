from typing import List

from pii.libraries.cache.redis_cache import r

# r.xadd("jdddddd", {"ffff": 'name ' + TimeUtil.int2str(TimeUtil.nowInt())})

tName = "jdddddd"
tName = "x:topic:all"
gName = "ggg"
cName = "ccc"

# ret = r.xread({keyName: "0"})
# r.xgroup_destroy(tName, gName)
# r.xgroup_create(tName, gName, '0')
tDesc = r.xinfo_stream(tName)
gDesc = r.xinfo_groups(tName)
ret = r.xreadgroup(gName, cName, {tName: ">"}, count=10, noack=True)

if ret:
    arr: List = ret[0][1]
    for one in arr:
        print(one)

pArr = r.xpending_range(tName, gName, "-", "+", count=50)
for one in pArr:
    r.xack(tName, gName, one["message_id"])

print()
