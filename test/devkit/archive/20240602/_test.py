# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-06-02 12:09:25 UTC+08:00
"""

from typing import Literal

_MARK_TYPE = Literal["release", "test", "alpha", "beta"]

print(_MARK_TYPE, type(_MARK_TYPE))
