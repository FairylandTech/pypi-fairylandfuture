# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-08-18 01:29:35 UTC+08:00
"""

__all__ = [
    "RESPONSE_CODE_MAPPING",
]


def __getattr__(name):
    """Lazy import."""
    if name == "RESPONSE_CODE_MAPPING":
        from fairylandfuture.const.http.response import RESPONSE_CODE_MAPPING
        return RESPONSE_CODE_MAPPING
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
