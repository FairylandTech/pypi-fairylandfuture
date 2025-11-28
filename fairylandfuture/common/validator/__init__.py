# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-08-10 17:38:14 UTC+08:00
"""

__all__ = [
    "ParamsValidator",
]


def __getattr__(name):
    """Lazy import."""
    if name == "ParamsValidator":
        from fairylandfuture.common.validator.validator import ParamsValidator
        return ParamsValidator
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
