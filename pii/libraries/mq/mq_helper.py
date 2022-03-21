import json
import re
from importlib import import_module

import time
from mq_http_sdk.mq_client import MQClient, sys
from mq_http_sdk.mq_consumer import MQConsumer
from mq_http_sdk.mq_producer import TopicMessage, MQExceptionBase, MQProducer

from pii import Pii
from pii.log import log

topic_id = Pii.config.get("pii.rocketmq.topic")
group_id = Pii.config.get("pii.rocketmq.group")
instance_id = Pii.config.get("pii.rocketmq.instance-id")

log.info(f"MQ topic: {topic_id}")


def fff(x):
    k, v = x
    return "%s=%s" % (k, v)


class MQ_Util:
    @staticmethod
    def out_q_consumer() -> MQConsumer:
        mq_client = MQClient(
            Pii.config.get("pii.rocketmq.endpoint"),
            Pii.config.get("pii.rocketmq.access-id"),
            Pii.config.get("pii.rocketmq.access-key"),
        )

        consumer = mq_client.get_consumer(instance_id, topic_id, group_id)
        return consumer

    @staticmethod
    def in_q(body: str = None):
        mq_client = MQClient(
            Pii.config.get("pii.rocketmq.endpoint"),
            Pii.config.get("pii.rocketmq.access-id"),
            Pii.config.get("pii.rocketmq.access-key"),
        )

        producer: MQProducer = mq_client.get_producer(instance_id, topic_id)

        try:
            msg = TopicMessage(message_tag="python.run", message_body=body)
            # msg.put_property("a", "i")  #
            # msg.set_message_key("MessageKey")  # KEY
            producer.publish_message(msg)

            # log.info("Publish Message Succeed. MessageID:%s, BodyMD5:%s" % (re_msg.message_id, re_msg.message_body_md5))
        except MQExceptionBase as e:
            if e.type == "TopicNotExist":
                log.error("Topic not exist, please create it.")
                sys.exit(1)
            log.error("Publish Message Fail. Exception: %s" % e)

        mq_client.close_connection()

    @staticmethod
    def genFunc(func, args: list, kwargs: dict, in_q: bool = False):
        clsArr = re.findall(r"function (\w+)\.", func.__str__())
        clsName = clsArr[0] if len(clsArr) == 1 else None

        ret = {
            "pkg": func.__module__,
            "cls": clsName,
            "func": func.__name__,
            # [1],
            "args": args,
            # {"b": "asd"}
            "kwargs": kwargs,
        }
        if in_q:
            MQ_Util.in_q(json.dumps(ret))
        return ret

    @staticmethod
    def callFunc(run: dict):
        pkg = import_module(run.get("pkg"))
        clsName = run.get("cls")
        funcName = run.get("func")
        if clsName is not None:
            cls = getattr(pkg, clsName)
            obj = cls()
            func = getattr(obj, funcName)
        else:
            func = getattr(pkg, funcName)
            # [1]
        args: list = run.get("args")
        # {"b": "asd"}
        kwargs: dict = run.get("kwargs")

        pStr = ", ".join(list(map(str, args)) + list(map(fff, kwargs.items())))
        log.info("MQ %s.%s(%s) ◷ start" % (clsName, funcName, pStr))
        mq_start = time.time()
        ret = func(*args, **kwargs)
        duration = str(format(int((time.time() - mq_start) * 1000), ","))
        log.info("MQ %s.%s(%s) ✔ done in %sms" % (clsName, funcName, pStr, duration))
        return ret


class CallTest:
    @staticmethod
    def jiafa(a):
        print(a + a)


def call_test(a, b="wqe"):
    print(a, b)
