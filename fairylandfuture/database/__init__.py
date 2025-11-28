# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-06-26 23:16:02 UTC+08:00
"""

__all__ = [
    # MySQL
    "CustomMySQLConnection",
    "CustomMySQLCursor",
    "MySQLConnector",
    "MySQLOperator",
    "MySQLSQLSimpleConnectionPool",
    # PostgreSQL
    "CustomPostgreSQLConnection",
    "CustomPostgreSQLCursor",
    "PostgreSQLConnector",
    "PostgreSQLOperator",
    "PostgreSQLSimpleConnectionPool",
    # Elasticsearch
    "ElasticSearchOperator",
]


def __getattr__(name):
    """Lazy import to avoid loading database drivers unless needed."""
    if name in ("CustomMySQLConnection", "CustomMySQLCursor", "MySQLConnector", "MySQLOperator", "MySQLSQLSimpleConnectionPool"):
        from fairylandfuture.database import mysql as _mysql
        return getattr(_mysql, name)
    if name in ("CustomPostgreSQLConnection", "CustomPostgreSQLCursor", "PostgreSQLConnector", "PostgreSQLOperator", "PostgreSQLSimpleConnectionPool"):
        from fairylandfuture.database import postgresql as _pg
        return getattr(_pg, name)
    if name == "ElasticSearchOperator":
        from fairylandfuture.database import elasticsearch as _es
        return getattr(_es, name)
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
