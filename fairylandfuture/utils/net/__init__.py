# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-06-02 02:42:33 UTC+08:00
"""

__all__ = [
    "LocalNetworkUtils",
]


def __getattr__(name):
    """Lazy import to avoid loading netifaces unless needed."""
    if name == "LocalNetworkUtils":
        from fairylandfuture.utils.net.local import LocalNetworkUtils
        return LocalNetworkUtils
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
