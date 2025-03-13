# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-08-25 13:45:27 UTC+08:00
"""

from fairylandfuture.core.superclass.decorators import BaseDecorator
from fairylandfuture.modules.decorators.methods import TryCatchMethodDecorator


@TryCatchMethodDecorator
class A:

    def a(self):
        print("a")


@TryCatchMethodDecorator
def a():
    a = 100 / 0


if __name__ == "__main__":
    # TryCatchMethodDecorator(a)()
    a()
