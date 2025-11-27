# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2025-11-25 12:25:58 UTC+08:00
"""

import unittest
from test import TestBase

from fairylandfuture.core.metaclass.singleton import SingletonMeta


class A(metaclass=SingletonMeta):

    def __init__(self):
        self.name = "Singleton A"


class Test(TestBase):

    def test_singleton(self):
        a1 = A()
        a2 = A()
        self.assertIs(a1, a2)
        print(f"a1 id: {id(a1)}, a2 id: {id(a2)}")


if __name__ == "__main__":
    unittest.main()
