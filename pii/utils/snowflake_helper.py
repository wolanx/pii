import random
import time

PtOffset = 1288834974657  # 不能改
Pa = 5  # 10位的数据机器位，可以部署在1024个节点，包括5位datacenterId和5位workerId
Pb = 5
Pc = 12  # 12位序列，毫秒内的计数，12位的计数顺序号支持每个节点每毫秒(同一机器，同一时间截)产生4096个ID序号
PtMax = 1 << (64 - Pa - Pb - Pc)
PaMax = 1 << Pa
PbMax = 1 << Pb
PcMax = 1 << Pc


class IdWorker:
    """
    1位标识，由于long基本类型在Java中是带符号的，最高位是符号位，正数是0，负数是1，所以id一般是正数，最高位是0
    41位时间截(毫秒级)，注意，41位时间截不是存储当前时间的时间截，而是存储时间截的差值（当前时间截 - 开始时间截)
    41位的时间截，可以使用69年，年T = (1L << 41) / (1000L * 60 * 60 * 24 * 365) = 69
    https://github.com/twitter/snowflake/blob/master/src/main/scala/com/twitter/service/snowflake/IdWorker.scala
    https://blog.csdn.net/zyt425916200/article/details/52775542
    https://github.com/falcondai/python-snowflake/blob/master/snowflake.py
    """

    @staticmethod
    def encode(ms: int, pa: int, pb: int, pc: int):
        sid = ((ms - PtOffset) % PtMax) << (Pa + Pb + Pc)
        sid += (pa % PaMax) << (Pb + Pc)
        sid += (pb % PbMax) << Pc
        sid += pc % PcMax

        return sid

    @staticmethod
    def decode(longId: int):
        pc = longId & (PcMax - 1)
        pb = (longId >> Pc) & (PbMax - 1)
        pa = (longId >> Pc >> Pb) & (PaMax - 1)
        ms = longId >> (Pa + Pb + Pc)
        ms += PtOffset

        return ms, pa, pb, pc

    @staticmethod
    def nextId():
        return IdWorker.encode(int(time.time() * 1000), 6300, 1, random.randint(0, 4096))


if __name__ == "__main__":
    t = int(time.time() * 1000)
    a = IdWorker.encode(t, 123, 123, 435235)
    b = IdWorker.decode(a)

    print(t)
    print(a)
    print(b)
