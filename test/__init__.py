# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2025-11-24 22:13:12 UTC+08:00
"""

import unittest


class TestBase(unittest.IsolatedAsyncioTestCase):

    def setUp(self):
        print(f" Start of {self._testMethodName} ".center(50, "="))

    def tearDown(self):
        print(f" End of {self._testMethodName} ".center(50, "=") + "\n")
