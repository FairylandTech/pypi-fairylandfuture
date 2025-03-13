# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-05-18 19:36:03 UTC+08:00
"""

import time

from fairylandfuture.modules.decorators import ActionDecorator, SingletonDecorator, TimingDecorator, TipsDecorator, TryCatchDecorator
from fairylandfuture.utils.journal import journal


class CustomTiming(TimingDecorator):

    def output(self, msg: str) -> None:
        journal.debug(msg)


class CustomAction(ActionDecorator):

    def output(self, msg: str) -> None:
        journal.debug(msg)


# @SingletonDecorator
class Person:
    me = 10

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @CustomTiming
    def get_name(self):
        time.sleep(0.5)
        return self.name

    @CustomAction(action="获取年龄的方法")
    def get_age(self):
        # raise Exception("xxxxxxx")
        return self.age

    def update_name(self, name):
        self.name = name
        return self.name

    @classmethod
    @CustomAction(action="类方法: 获取 me")
    def get_me(cls):
        return cls.me

    @staticmethod
    @CustomAction(action="静态方法: 获取实参")
    def get_(aa):
        return aa

    @staticmethod
    @CustomAction(action="静态方法: 无形参")
    def get__():
        return "123123"


@CustomAction(action="普通函数: 无参数")
def test_1():
    return "test_1"


if __name__ == "__main__":
    alice = Person("alice", 11)
    jack = Person("jack", 12)
    journal.debug(alice is jack)

    journal.debug(alice.get_name())
    journal.debug(alice.get_age())

    journal.debug(jack.get_age())
    journal.debug(alice.get_(aa="123123123"))
    journal.debug(alice.get__())
    journal.debug(alice.get_me())

    journal.debug(test_1())
