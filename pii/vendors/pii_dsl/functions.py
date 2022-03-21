import math
from datetime import timedelta

import numpy as np

from libraries.tsdb.opentsdb_helper import OpentsUtil
from libraries.tsdb.tsdb_helper import TSdbUtil
from pii.libraries.utils.time_util import TimeUtil
from model.gf_device_attr import DeviceAttrModel
from pii.vendors.pii_dsl.PiiDsl.PiiDslParser import PiiDslParser
from service.device_service import DeviceService


def sin(model: dict, argsCtx, argsKey: list, argsVal: list):
    return math.sin(argsVal[0])


def cos(model: dict, argsCtx, argsKey: list, argsVal: list):
    return math.cos(argsVal[0])


def DeviceRef(model: dict, argsCtx, argsKey: list, argsVal: list):
    did = argsVal[0]
    metric = argsKey[1]
    dssObj = DeviceService.getOneSpec(did).getMetric()
    return dssObj.get(metric)


def Integrate(model: dict, argsCtx, argsKey: list, argsVal: list):
    sourceMetric = argsKey[0]
    targetMetric = model.get("targetMetric")
    did = model.get("device_id")
    deviceTs = TimeUtil.nowInt()
    lTs = argsVal[2]

    sourceObj = DeviceAttrModel.get_or_none(alias=sourceMetric)
    targetObj = DeviceAttrModel.get_or_none(alias=targetMetric)

    sourceSn = DeviceService.getSN(did, sourceObj.id) if sourceObj else None
    targetSn = DeviceService.getSN(did, targetObj.id) if targetObj else None

    rTime = TimeUtil.int2date(deviceTs)
    if lTs > 0:
        targetPoint = TSdbUtil.getLastOne(targetSn, targetMetric, ts=deviceTs)
        y_1ms = targetPoint.get("timestamp")
        if y_1ms is None:
            # y(0) = ∫(lTime ~ rTime)
            lTime = TimeUtil.int2date(lTs)
            bucket = TimeUtil.autoTsdbBucket(lTime, rTime)

            res: dict = TSdbUtil.aggByMetric(
                sn=sourceSn,
                metric=sourceMetric,
                start=TimeUtil.date2stamp(lTime),
                end=TimeUtil.date2stamp(rTime),
                agg="avg",
                bucket=bucket,
            )
            x, y = list(res.keys()), list(res.values())
            x = np.array(x, dtype=np.float64)
            y = np.array(y, dtype=np.float64)
            y = np.nan_to_num(y, nan=0)

            out = np.trapz(y=y, x=x)
        else:
            # y(0) = y(-1) + ∫(y(-1).ts ~ rTime)
            lTime = TimeUtil.int2date(y_1ms / 1000)
            x = (rTime - lTime).seconds
            sourcePoint = TSdbUtil.getLastOne(sourceSn, sourceMetric, ts=deviceTs)
            y = sourcePoint.get("value", 0)

            out = targetPoint.get("value") + x * y
    else:
        lTime = TimeUtil.int2date(deviceTs) + timedelta(seconds=lTs)
        bucket = TimeUtil.autoTsdbBucket(lTime, rTime)

        res: dict = TSdbUtil.aggByMetric(
            sn=sourceSn,
            metric=sourceMetric,
            start=TimeUtil.date2stamp(lTime),
            end=TimeUtil.date2stamp(rTime),
            agg="avg",
            bucket=bucket,
        )
        x, y = list(res.keys()), list(res.values())
        x = np.array(x, dtype=np.float64)
        y = np.array(y, dtype=np.float64)
        y = np.nan_to_num(y, nan=0)

        out = np.trapz(y=y, x=x)

    return out


def TimeShift(model: dict, argsCtx, argsKey: list, argsVal: list):
    metric = argsKey[0]
    offset = argsVal[1]
    did = model.get("device_id")
    #
    attrObj = DeviceAttrModel.get_or_none(alias=metric)
    dssObj = DeviceService.getOneSpec(did).getMetric()
    deviceTs = dssObj.get("ts")
    deviceTs = deviceTs if deviceTs else TimeUtil.nowInt()

    if attrObj is None:
        sn = None
    else:
        sn = DeviceService.getSN(did, attrObj.id)
    targetTs = deviceTs + offset
    target: dict = TSdbUtil.getLastMetricMapByTs({metric: sn}, targetTs)
    return target.get(metric)


def CountIf(model: dict, argsCtx, argsKey: list, argsVal: list):
    ctx0: PiiDslParser.EqualityExprContext = argsCtx[0]
    lTs = argsVal[1]
    metric = ctx0.expr(0).getText()
    target = int(ctx0.expr(1).getText())
    attrObj = DeviceAttrModel.get_or_none(alias=metric)
    did = model.get("device_id")
    dssObj = DeviceService.getOneSpec(did).getMetric()
    deviceTs = dssObj.get("ts")
    deviceTs = deviceTs if deviceTs else TimeUtil.nowInt()

    if attrObj is None:
        sn = None
    else:
        sn = DeviceService.getSN(did, attrObj.id)

    # v new
    # rows, _ = TSdbUtil.doQuery(
    #     f'select count("{metric}") as value from sensor_0s'
    #     f' where SNO = "{sn}" and "{metric}" = {target}'
    #     f" and time >= {deviceTs + lTs}s and time <= {deviceTs}s"
    # )
    #
    # return rows[0].get("value") if len(rows) else 0

    # v old
    lTime = TimeUtil.int2date(deviceTs) + timedelta(hours=-8) + timedelta(seconds=lTs)
    rTime = TimeUtil.int2date(deviceTs) + timedelta(hours=-8)
    sql = f"""
    SELECT count(`value`)
    FROM `tsdb`.`{metric}`
    WHERE `SNO` = '{sn}' AND `value` = {target} AND `timestamp` BETWEEN '{lTime}' AND '{rTime}'
    """

    rows, err = OpentsUtil.runSql(sql)
    if err or len(rows) == 0:
        return None
    row = rows[0]  # type: dict
    return int(row.get("EXPR$0"))


funcs = {
    "sin": sin,
    "cos": cos,
    "DeviceRef": DeviceRef,
    "Integrate": Integrate,
    "TimeShift": TimeShift,
    "CountIf": CountIf,
}
