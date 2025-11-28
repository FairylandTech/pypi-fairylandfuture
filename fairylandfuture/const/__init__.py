# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-05-09 18:44:28 UTC+08:00
"""

__all__ = [
    "RESPONSE_CODE_MAPPING",
]


def __getattr__(name):
    """Lazy import."""
    if name == "RESPONSE_CODE_MAPPING":
        from fairylandfuture.const.http import RESPONSE_CODE_MAPPING
        return RESPONSE_CODE_MAPPING
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
