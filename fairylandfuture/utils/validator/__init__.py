# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2025-05-16 17:43:26 UTC+08:00
"""

__all__ = [
    "StringValidatorUtils",
]


def __getattr__(name):
    """Lazy import."""
    if name == "StringValidatorUtils":
        from fairylandfuture.utils.validator.strings import StringValidatorUtils
        return StringValidatorUtils
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")