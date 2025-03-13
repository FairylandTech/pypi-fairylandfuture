# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-05-18 10:52:17 UTC+08:00
"""

import time
from functools import wraps
from typing import Any, Callable, Generic, Literal, Optional, Type, TypeVar

from fairylandfuture.modules.decorators import ActionDecorator
from fairylandfuture.modules.decorators import TimingDecorator
from fairylandfuture.modules.decorators import TipsDecorator
from fairylandfuture.modules.decorators import TryCatchDecorator
from fairylandfuture.utils.journal import journal

_T = TypeVar("_T", bound=Callable[..., Any])


class CustomTiming(TimingDecorator):

    def output(self, msg: str) -> None:
        print(msg)


class CustomAction(ActionDecorator):

    def output(self, msg: str) -> None:
        print(msg)


class CustomTips(TipsDecorator):

    def output(self, msg: str) -> None:
        journal.debug(msg)


#
#
# class A:
#
#     def __init__(self, a):
#         self.a = a
#
#     def out(self):
#         print(self.a)
#
#
# class B:
#
#     def __init__(self, b):
#         self.b = b
#
#     @ActionDecorator(action="out")
#     def out(self):
#         print(self.b)
#
#
# @CustomTips(tips="函数aa")
# def aa(a):
#     print(a)
#
#
# @CustomAction(action="函数bb")
# def bb(b):
#     print(b)


@CustomTiming
@CustomAction(action="无参数的普通函数")
def func1():
    time.sleep(0.2)
    print("Done.")


@CustomTiming
@CustomAction(action="有参数的普通函数")
def func2(x, y):
    print(f"2个参数之和: {x + y}")
    time.sleep(2)


class TestFunc:

    @CustomTiming
    @CustomAction(action="无参数的实例方法")
    def test1(self):
        time.sleep(0.2)

    @CustomTiming
    @CustomAction(action="有参数的实例方法")
    def test2(self, x, y):
        print(f"2个参数之和: {x + y}")
        time.sleep(0.2)

    @classmethod
    @CustomTiming
    @CustomAction(action="无参数的类方法")
    def test3(cls):
        time.sleep(0.2)

    @classmethod
    @CustomTiming
    @CustomAction(action="有参数的类方法")
    def test4(cls, x, y):
        print(f"2个参数之和: {x + y}")
        time.sleep(0.2)

    @staticmethod
    @CustomTiming
    @CustomAction(action="无参数的静态方法")
    def test5():
        time.sleep(0.2)

    @staticmethod
    @CustomTiming
    # @CustomAction(action="有参数的静态方法")
    @CustomAction()
    @CustomTips(tips="有参数的静态方法")
    def test6(x, y):
        print(f"2个参数之和: {x + y}")
        time.sleep(0.2)


if __name__ == "__main__":
    func1()
    print("-" * 50)
    func2(1, 1)
    print("-" * 50)
    tf = TestFunc()
    tf.test1()
    print("-" * 50)
    tf.test2(1, 1)
    print("-" * 50)
    tf.test3()
    print("-" * 50)
    tf.test4(1, 1)
    print("-" * 50)
    tf.test5()
    print("-" * 50)
    tf.test6(1, 1)
