# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2025-05-28 17:17:01 UTC+08:00
"""

__all__ = [
    "UserAgentParserHelper",
]


def __getattr__(name):
    """Lazy import to avoid loading user_agents module unless needed."""
    if name == "UserAgentParserHelper":
        from fairylandfuture.helpers.parser.ua import UserAgentParserHelper
        return UserAgentParserHelper
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
