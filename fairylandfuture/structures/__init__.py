# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-06-25 13:43:10 UTC+08:00
"""

__all__ = [
    # Database
    "MySQLExecuteFrozenStructure",
    "PostgreSQLExecuteFrozenStructure",
    "ElasticsearchBulkParamFrozenStructure",
    # HTTP
    "HTTPSimpleRequestResultStructure",
    "ResponseStructure",
    "ResponseFrozenStructure",
]


def __getattr__(name):
    """Lazy import to avoid circular dependencies."""
    if name in ("MySQLExecuteFrozenStructure", "PostgreSQLExecuteFrozenStructure", "ElasticsearchBulkParamFrozenStructure"):
        from fairylandfuture.structures import database as _db
        return getattr(_db, name)
    if name in ("HTTPSimpleRequestResultStructure", "ResponseStructure", "ResponseFrozenStructure"):
        from fairylandfuture.structures import http as _http
        return getattr(_http, name)
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
