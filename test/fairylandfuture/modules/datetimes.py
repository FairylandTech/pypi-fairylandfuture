# coding: utf-8

from fairylandfuture.modules.datetimes import DateTimeModule


class TestDataTime:

    @classmethod
    def run(cls):
        method_list = [func for func in dir(cls) if callable(getattr(cls, func)) and not func.startswith("__")]
        for method in method_list:
            if method.startswith("test_"):
                getattr(cls, method)()

    @classmethod
    def test_001(cls):
        print("获取当前日期")
        print(DateTimeModule.DATE())
        print(DateTimeModule.DATE(_format="%Y-%m-%d"))
        print(DateTimeModule.DATE(_format="%Y%m%d"))
        print(DateTimeModule.DATE(_format="%Y%m%d %I:%M %p"))
        print("=======================")

    @classmethod
    def test_002(cls):
        print("获取当前时间")
        print(DateTimeModule.TIME())
        print(DateTimeModule.TIME(_fromat="%H:%M:%S"))
        print("=======================")

    @classmethod
    def test_003(cls):
        print("获取当前日期时间")
        print(DateTimeModule.DATETIME())
        print(DateTimeModule.DATETIME(_format="%Y-%m-%d %H:%M:%S"))
        print("=======================")

    @classmethod
    def test_004(cls):
        print("获取当前时间戳")
        print(DateTimeModule.timestamp())
        print(DateTimeModule.timestamp(millisecond=False))
        print(DateTimeModule.timestamp(millisecond=True))
        print(DateTimeModule.timestamp(n=13))
        print(DateTimeModule.timestamp(n=15))
        print("=======================")

    @classmethod
    def test_005(cls):
        print("获取昨天的日期")
        print(DateTimeModule.yesterday())
        print(DateTimeModule.yesterday(_format="%Y-%m-%d"))
        print(DateTimeModule.yesterday(_format="%m-%d-%Y-%I:%M %p"))
        print("=======================")

    @classmethod
    def test_006(cls):
        print("获取明天的日期")
        print(DateTimeModule.tomorrow())
        print(DateTimeModule.tomorrow(_format="%Y-%m-%d"))
        print(DateTimeModule.tomorrow(_format="%m-%d-%Y-%I:%M %p"))
        print("=======================")

    @classmethod
    def test_007(cls):
        print("日期时间字符串时间戳")
        print(DateTimeModule.datetime_to_timestamp(datetime_string="2000-01-01 00:01:00"))
        print(DateTimeModule.datetime_to_timestamp(datetime_string="2000-01-01 00:01:00", millisecond=True))
        print(DateTimeModule.datetime_to_timestamp(datetime_string="2000-01-01 00:01:00", n=13))
        print(DateTimeModule.datetime_to_timestamp(datetime_string="2000-01-01 00:01:00", n=15))
        # print(DateTimeModule.datetime_to_timestamp("June 03, 2024 10:06 PM", _format="%B %d, %Y %I:%M %p"))
        print(DateTimeModule.datetime_to_timestamp(datetime_string="June 03, 2024 10:06 PM", _format="%B %d, %Y %I:%M %p"))
        print("=======================")

    @classmethod
    def test_008(cls):
        print("时间戳转日期时间字符串")
        # print(DateTimeModule.timestamp())
        print(DateTimeModule.timestamp_to_datetime(DateTimeModule.timestamp(), _format="%B %d, %Y %I:%M %p"))
        print(DateTimeModule.timestamp_to_datetime(timestamp=1717430250))
        print(DateTimeModule.timestamp_to_datetime(timestamp=1717431007265, _format="%Y-%b-%d %I:%M:%S"))
        print("=======================")

    @classmethod
    def test_009(cls):
        print("时间戳转日期时间字符串")
        print(DateTimeModule.daysdelta(dt1="2010-10-14", dt2="2010-10-12"))
        print(DateTimeModule.daysdelta(dt1="2010-10-14", dt2="2010-10-12", _format="%Y-%m-%d"))
        print(DateTimeModule.daysdelta(dt1="2010-10-14", dt2="2010-10-16", _format="%Y-%m-%d"))
        print(DateTimeModule.daysdelta(dt1=1717329938, dt2=1717430250, timestamp=True))
        print(DateTimeModule.daysdelta(dt1=1717329938000, dt2=1717502738878, timestamp=True, millisecond=True))
        print("=======================")


if __name__ == "__main__":
    TestDataTime.run()
