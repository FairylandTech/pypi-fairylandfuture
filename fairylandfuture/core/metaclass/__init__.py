# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-07-03 22:53:26 UTC+08:00
"""

__all__ = [
    "SingletonMeta",
]


def __getattr__(name):
    """Lazy import for consistency with other modules."""
    if name == "SingletonMeta":
        from fairylandfuture.core.metaclass.singleton import SingletonMeta
        return SingletonMeta
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
