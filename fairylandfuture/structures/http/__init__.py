# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-08-14 17:01:45 UTC+08:00
"""

__all__ = [
    "HTTPSimpleRequestResultStructure",
    "ResponseStructure",
    "ResponseFrozenStructure",
]


def __getattr__(name):
    """Lazy import to avoid circular dependencies."""
    if name == "HTTPSimpleRequestResultStructure":
        from fairylandfuture.structures.http.request import HTTPSimpleRequestResultStructure
        return HTTPSimpleRequestResultStructure
    if name in ("ResponseStructure", "ResponseFrozenStructure"):
        from fairylandfuture.structures.http import response as _resp
        return getattr(_resp, name)
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
