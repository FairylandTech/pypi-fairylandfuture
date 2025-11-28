# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2025-09-10 23:17:38 UTC+08:00
"""

__all__ = [
    "HTTPRequestMethodEnum",
]


def __getattr__(name):
    """Lazy import."""
    if name == "HTTPRequestMethodEnum":
        from fairylandfuture.enums.http.request import HTTPRequestMethodEnum
        return HTTPRequestMethodEnum
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")