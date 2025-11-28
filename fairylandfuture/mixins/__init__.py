# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2025-02-17 10:30:39 UTC+08:00
"""

__all__ = [
    "DRFResponseMixin",
]


def __getattr__(name):
    """Lazy import to avoid loading DRF unless needed."""
    if name == "DRFResponseMixin":
        from fairylandfuture.mixins.drf import DRFResponseMixin
        return DRFResponseMixin
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
