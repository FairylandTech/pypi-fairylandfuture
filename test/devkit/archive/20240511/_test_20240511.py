# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-05-11 13:53:27 UTC+08:00
"""

# 时间模块
from fairylandfuture.modules.datetimes import DateTimeModule

# 注解
from fairylandfuture.modules.decorators import ActionDecorator, TimingDecorator

# 日志
from fairylandfuture.modules.journal import journal

# 枚举


class TestDateTimeModule:

    @classmethod
    @TimingDecorator
    def run(cls):
        method_list = [func for func in dir(cls) if callable(getattr(cls, func)) and not func.startswith("__")]
        for method in method_list:
            if method.startswith("test_"):
                getattr(cls, method)()

    @classmethod
    @ActionDecorator(action="日期转时间戳")
    def test_datetime_to_timestamp(cls):
        _date = "2024-05-11"
        _time = "13:53:27"
        timestamp = DateTimeModule.datetime_to_timestamp(" ".join((_date, _time)))
        journal.debug(timestamp)


if __name__ == "__main__":
    TestDateTimeModule.run()

    with open("../conf/publish/.commitrc", "r", encoding="UTF-8") as f:
        r = f.read()
    print(int(r))
