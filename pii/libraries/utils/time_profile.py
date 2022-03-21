from datetime import datetime, timedelta
from time import sleep


class TimeProfile:
    """
    timestamp efficiency statistics
    """

    name = ""
    res = []

    def __init__(self, name=""):
        self.name = name
        self.res = []
        self.point()

    def point(self, scope="name"):
        self.res.append((scope, datetime.now()))

    def table(self):
        """
        1.990 [111]	|∎∎∎∎∎∎∎∎∎∎
        2.620 [50]	|∎∎∎∎
        3.250 [12]	|∎
        @return:
        """
        max_ = 0
        ret = []

        print("Summary:")
        print("  Name :", self.name)
        print("  Total:", self.res[-1][1] - self.res[0][1])
        print("Response time histogram:")

        for i in range(len(self.res) - 1):
            (_, a) = self.res[i]
            (name, b) = self.res[i + 1]
            diff: timedelta = b - a
            t = diff.seconds + diff.microseconds / 1e6
            if t > max_:
                max_ = t

            ret.append({"t": t, "n": name, "c": 0})

        for r in ret:
            c_pct = round(r["t"] / max_, 2)
            c_num = int(c_pct * 50)
            print("  [{0:<18.18}] {1:>5.2f}s | {2:>6.1%} {3}".format(r["n"], r["t"], c_pct, "∎" * c_num))


if __name__ == "__main__":
    """
    demo
    """
    tp = TimeProfile()

    sleep(0.3)
    tp.point("qwerasdfzxcv")

    sleep(0.2)
    tp.point()

    sleep(0.4)
    tp.point("c")

    tp.table()
