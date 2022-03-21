from unittest import TestCase

from pii.vendors.pii_dsl import PiiDsl
from service.device_service import DeviceService


class TestTSdbUtil(TestCase):
    def c(self, a, b, ctx: dict = None):
        self.assertEqual(a, PiiDsl(b).out(ctx), b)

    def test_1_base(self):
        self.c(66, "33 * 2")
        self.c(4.0, "32 / 8")
        self.c(5, "1 + 2 * 2")
        self.c(0.5, "3 / (3 + 3)")

    def test_2_assign(self):
        self.c(
            5,
            """
            b = 1
            c = 2
            b + c * 2
            """,
        )
        self.c(
            10,
            """
            b = 3
            b = b * b
            b + 1
            """,
        )

    def test_3_func_1(self):
        self.c(0.9092974268256817, "sin(2)")
        self.c(-0.4161468365471424, "cos(2)")

    def test_3_func_DeviceRef(self):
        v = PiiDsl("DeviceRef(126, ai1)").out()
        print(v)
        assert v > 100
        assert v < 200

    def test_3_func_Integrate(self):
        v = PiiDsl("Integrate(ai1, t, 1617206400, 0) / 1").out(dict(device_id=126))
        print(v)
        assert v > 100000

    def test_3_func_TimeShift(self):
        dssObj = DeviceService.getOneSpec(126)
        ctx = dssObj.getMetric()
        v = PiiDsl("ai1 - TimeShift(ai1, -3600)").out(ctx)
        print(v)
        assert v > -50
        assert v < 50

    def test_3_func_CountIf(self):
        dssObj = DeviceService.getOneSpec(126)
        ctx = dssObj.getMetric()
        v = PiiDsl("CountIf(w1 == 1, -3600, 0)").out(ctx)
        print(v)
        assert v > 1
        v = PiiDsl("CountIf(w1 == 1, -3600, 0) > 1").out(ctx)
        print(v)
        assert v is True

    def test_b_base(self):
        self.c(True, "1 < 2")
        self.c(False, "1 > 2")
        self.c(True, "1 <= 2")
        self.c(False, "1 >= 2")
        self.c(False, "1 == 2")
        self.c(True, "1 != 2")

        self.c(True, "1 + 2 > 2")
        self.c(3, "2 + (2 > 1)")
