# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-05-12 02:24:21 UTC+08:00
"""

import os
from datetime import datetime

from _test import TestBase
from dateutil.relativedelta import relativedelta

from fairylandfuture.enums.chrono import DateTimeEnum
from fairylandfuture.modules.datetimes import DateTimeModule
from fairylandfuture.modules.decorators import ActionDecorator, SingletonDecorator, TimingDecorator, TipsDecorator
from fairylandfuture.utils.journal import journal


class CustomizeTimingDecorator(TimingDecorator):
    def output(self, msg: str) -> None:
        journal.debug(msg)


class CustomizeActionDecorator(ActionDecorator):
    def output(self, msg: str) -> None:
        journal.debug(msg)


class TestClass(TestBase):

    @classmethod
    @TipsDecorator(tips="测试001")
    def test_001(cls):
        journal.debug(DateTimeModule.timestamp())

    @classmethod
    @CustomizeActionDecorator(action="测试002")
    def test_002(cls):
        a = datetime.now() - relativedelta(days=1)
        journal.debug(a.strftime(DateTimeEnum.TIME_CN.value))

    @classmethod
    @CustomizeTimingDecorator
    @CustomizeActionDecorator(action="测试003")
    def test_003(cls):
        a = DateTimeModule.daysdelta("2024/05/12", "2024/05/25", _format="%Y/%m/%d")
        b = DateTimeModule.datetime_to_timestamp("2024/05/12", millisecond=False, _format="%Y/%m/%d")
        c = DateTimeModule.datetime_to_timestamp("2024--05--25", millisecond=False, _format="%Y--%m--%d")
        d = DateTimeModule.daysdelta(b, c, timestamp=True)
        journal.debug(a)
        journal.debug(b)
        journal.debug(c)
        journal.debug(d)

    @classmethod
    def test_004(cls):
        def a():
            pass

    @classmethod
    def test_005(cls):
        logs_dir = "logs"
        logs_file = "test.log"
        a = os.path.join(logs_dir, logs_file)
        journal.debug(a)
        journal.debug(type(a))

    @classmethod
    def test_006(cls):
        a = "s"
        n, e = os.path.splitext(a)
        # print(repr(n), repr(e))


@SingletonDecorator
class A:

    @classmethod
    def get(cls):
        return "get"


def aa():
    pass


if __name__ == "__main__":
    TestClass.run()
