# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-08-18 01:03:44 UTC+08:00
"""

__all__ = [
    "AbstractMySQLOperator",
    "AbstractPostgreSQLOperator",
]


def __getattr__(name):
    """Lazy import to avoid circular dependencies."""
    if name in ("AbstractMySQLOperator", "AbstractPostgreSQLOperator"):
        from fairylandfuture.abstract import database as _db
        return getattr(_db, name)
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")