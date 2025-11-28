# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-08-25 13:41:51 UTC+08:00
"""

__all__ = [
    "TryCatchMethodDecorator",
]


def __getattr__(name):
    """Lazy import."""
    if name == "TryCatchMethodDecorator":
        from fairylandfuture.decorators.methods import TryCatchMethodDecorator
        return TryCatchMethodDecorator
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
