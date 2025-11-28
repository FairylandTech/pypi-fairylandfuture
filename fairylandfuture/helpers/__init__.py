# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-05-12 14:42:50 UTC+08:00
"""

__all__ = [
    # JSON
    "JsonEncoder",
    "JsonSerializerHelper",
    # Parser
    "UserAgentParserHelper",
]


def __getattr__(name):
    """Lazy import to avoid circular dependencies."""
    if name in ("JsonEncoder", "JsonSerializerHelper"):
        from fairylandfuture.helpers import json as _json
        return getattr(_json, name)
    if name == "UserAgentParserHelper":
        from fairylandfuture.helpers import parser as _parser
        return getattr(_parser, name)
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
