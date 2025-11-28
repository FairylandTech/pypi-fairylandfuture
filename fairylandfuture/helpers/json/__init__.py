# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2025-05-14 10:47:53 UTC+08:00
"""

__all__ = [
    "JsonEncoder",
    "JsonSerializerHelper",
]


def __getattr__(name):
    """Lazy import to avoid circular dependencies."""
    if name == "JsonEncoder":
        from fairylandfuture.helpers.json.encoder import JsonEncoder
        return JsonEncoder
    if name == "JsonSerializerHelper":
        from fairylandfuture.helpers.json.serializer import JsonSerializerHelper
        return JsonSerializerHelper
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
