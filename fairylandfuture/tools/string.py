# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2025-03-12 00:00:41 UTC+08:00
"""
import re

class StringTools(object):

    @classmethod
    def to_plain(cls, metastr: str):
        plain = re.sub(r'\s+', ' ', metastr.strip())

        return plain
