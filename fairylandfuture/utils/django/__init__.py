# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2025-11-28 12:18:47 UTC+08:00
"""

__all__ = [
    "DjangoRequestUtils",
]


def __getattr__(name):
    """Lazy import to avoid loading Django unless needed."""
    if name == "DjangoRequestUtils":
        from fairylandfuture.utils.django.request import DjangoRequestUtils
        return DjangoRequestUtils
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")