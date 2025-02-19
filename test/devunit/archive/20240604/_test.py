# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-06-04 12:08:02 UTC+08:00
"""

# from fairylandfuture.utils.journal import journal
from fairylandfuture.core.superclass.enums.enumerate import BaseEnum


class DepartmemtEnum(BaseEnum):
    PART1 = "第一部门"
    PART2 = "第二部门"
    DEFAULT = "默认部门"

    @classmethod
    def default(cls):
        return cls.DEFAULT.value


if __name__ == "__main__":
    # journal.debug(f"2024-05-20 00:00:00 转为unix时间戳: {DateTimeModule.datetime_to_timestamp('2024-05-20 00:00:00', millisecond=True)}")
    # journal.debug(f"2024-06-10 00:00:00 转为unix时间戳: {DateTimeModule.datetime_to_timestamp('2024-06-10 00:00:00', millisecond=True)}")
    # journal.debug(f"{DateTimeModule.timestamp_to_datetime(1717477912000)}")
    # journal.debug(f"{DateTimeModule.timestamp_to_datetime(1717478032000)}")
    # journal.debug(f"{DateTimeModule.timestamp_to_datetime(1716134400000)}")
    # journal.debug(f"{DateTimeModule.timestamp_to_datetime(1717948800000)}")
    # part1_name = DepartmemtEnum.PART1.value
    # journal.debug(f"{part1_name}")

    # # print(DepartmemtEnum.get("PART1"))
    # print(DepartmemtEnum.names())
    # print(DepartmemtEnum.values())

    print(DepartmemtEnum.default())
