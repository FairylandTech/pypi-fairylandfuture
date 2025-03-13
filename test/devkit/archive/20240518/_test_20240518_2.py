# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-05-18 13:00:17 UTC+08:00
"""

import time
from functools import wraps


class TimeDecorator:
    def __init__(self, func):
        wraps(func)(self)
        self.func = func

    def __call__(self, *args, **kwargs):
        start_time = time.time()
        result = self.func(*args, **kwargs)
        end_time = time.time()
        self.total_time = end_time - start_time
        self.output()
        return result

    def output(self):
        print(f"Function {self.func.__name__} took {self.total_time:.6f} seconds.")

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return self.__class__(self.func.__get__(instance, owner))


# 使用示例


# 为普通函数装饰
@TimeDecorator
def my_function(x, y):
    time.sleep(1)
    return x + y


# 为类方法装饰
class MyClass:
    @TimeDecorator
    def my_method(self, x, y):
        time.sleep(1)
        return x * y

    @classmethod
    @TimeDecorator
    def my_classmethod(cls, x, y):
        time.sleep(1)
        return x**y

    @staticmethod
    @TimeDecorator
    def my_staticmethod(x, y):
        time.sleep(1)
        return x - y


# 自定义输出
class CustomOutputTimeDecorator(TimeDecorator):
    def output(self):
        print(f"[Custom Output] {self.func.__name__} completed in {self.total_time:.6f} seconds.")


# 为函数装饰自定义输出
@CustomOutputTimeDecorator
def my_custom_function(x, y):
    time.sleep(1)
    return x / y


class MyClass2:

    @CustomOutputTimeDecorator
    def a(self):
        print("aa")

    @CustomOutputTimeDecorator
    def aa(self, a):
        print(a)


# 测试
my_function(3, 4)
MyClass().my_method(3, 4)
MyClass.my_classmethod(3, 4)
MyClass.my_staticmethod(3, 4)
my_custom_function(3, 4)
a = MyClass2()
a.a()
a.aa(3)
