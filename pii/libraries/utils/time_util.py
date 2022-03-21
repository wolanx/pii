import itertools
import math
from datetime import datetime, date, timedelta

import time


class TimeUtil:
    @staticmethod
    def msUse(a) -> str:
        b = datetime.now()
        diff: timedelta = b - a
        ms = int((diff.seconds + diff.microseconds / 1e6) * 1000)
        return "{:>5} ms".format(ms)

    @staticmethod
    def genDateRange(start=-7, end=-1, data_type: None or int = None):
        """
        e.g. TimeUtil.genDateRange(-7, -1, data_type=int) [1577116800, 1577203200, 1577289600, 1577376000, 1577462400, 1577548800, 1577635200]
        7ds = -7~-1
        0 today，-1 yesterday
        @param start:
        @param end:
        @param data_type: return default datetime，int
        @return: created date
        """
        ret = []

        today = time.mktime(date.today().timetuple())
        ts = datetime.fromtimestamp(today)

        for gap in range(start, end + 1):
            gap_ = ts + timedelta(days=gap)
            if data_type == int:
                ret.append(int(gap_.timestamp()))
            else:
                ret.append(gap_)

        return ret

    @staticmethod
    def int2str(ts, str_format="%Y-%m-%d %H:%M:%S"):
        return time.strftime(str_format, time.localtime(ts))

    @staticmethod
    def int8toStrZ(ts: int) -> str:
        return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.localtime(ts))

    @staticmethod
    def int2date(ts):
        return datetime.fromtimestamp(ts)

    @staticmethod
    def str2int(tss1, tformat="%Y-%m-%d %H:%M:%S"):
        """utc 自动转换"""
        if tss1 == "0000-00-00 00:00:00":
            return 0
        utcdate = datetime.strptime(tss1, tformat)
        return int(utcdate.timestamp())

    @staticmethod
    def nowInt():
        return int(time.time())

    @staticmethod
    def str2date(s, str_format="%Y-%m-%d %H:%M:%S"):
        return datetime.strptime(s, str_format)

    @staticmethod
    def str2dateZ(s):
        return datetime.strptime(s, "%Y-%m-%dT%H:%M:%SZ")

    @staticmethod
    def date2str(dt: datetime, str_format="%Y-%m-%d %H:%M:%S"):
        return dt.strftime(str_format)

    @staticmethod
    def date2strZ(dt: datetime):
        return dt.strftime("%Y-%m-%dT%H:%M:%SZ")

    @staticmethod
    def date2stamp(t):
        return int(time.mktime(t.timetuple()))

    @staticmethod
    def get_raw_stamp(stamp: int):
        time_str = TimeUtil.int2str(stamp, str_format="%Y-%m-%d %H:%M:00")
        return TimeUtil.str2int(time_str)

    def __range_diff(r1, r2):
        s1, e1 = r1
        s2, e2 = r2
        endpoints = sorted((s1, s2, e1, e2))
        result = []
        if endpoints[0] == s1:
            result.append((endpoints[0], endpoints[1]))
        if endpoints[3] == e1:
            result.append((endpoints[2], endpoints[3]))
        return result

    @staticmethod
    def multirange_diff(r1_list, r2_list):
        # r1 - r2 差集
        result = []
        if len(r2_list) <= 0:
            return r1_list
        # if (r1_list[-1][-1] <= r2_list[0][0]) or (r1_list[0][0] >= r2_list[-1][-1]):
        #     return r1_list
        for r2 in r2_list:
            r1_list = list(itertools.chain(*[TimeUtil.__range_diff(r1, r2) for r1 in r1_list]))
            result = [each for each in r1_list if each[0] != each[1]]
        return result

    @staticmethod
    def merge_periods(intervals):
        sorted_by_lower_bound = sorted(intervals, key=lambda tup: tup[0])
        merged = []

        for higher in sorted_by_lower_bound:
            if not merged:
                merged.append(higher)
            else:
                lower = merged[-1]
                # test for intersection between lower and higher:
                if higher[0] <= lower[1]:
                    upper_bound = max(lower[1], higher[1])
                    merged[-1] = (lower[0], upper_bound)  # replace by merged interval
                else:
                    merged.append(higher)
        return merged

    @staticmethod
    def autoTsdbBucket(lTime: datetime, rTime: datetime, pct: float = 1):
        epoch = (rTime - lTime) * (pct / 100)
        if epoch.days > 0:
            bucket = f"{epoch.days}d"
        else:
            m = math.floor(epoch.seconds / 60)
            m = max(m, 1)
            bucket = str(m) + "m"

        return bucket


if __name__ == "__main__":
    a = TimeUtil.genDateRange()
    for i in a:
        print(i)

    a = TimeUtil.genDateRange(data_type=int)
    for i in a:
        print(i)
