# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-08-10 18:26:51 UTC+08:00
"""

__all__ = [
    # Database
    "SQLExecutionException",
    "SQLSyntaxException",
    # Elasticsearch
    "ElasticSearchExecutionException",
    # File
    "FileReadException",
    # Generic
    "ParamsInvalidException",
    "ParamsTypeException",
    "ParamsValueException",
    "ValidationError",
    # Messages
    "SQLSyntaxExceptMessage",
    "ElasticSearchExceptMessage",
]


def __getattr__(name):
    """Lazy import to avoid circular dependencies."""
    if name in ("SQLExecutionException", "SQLSyntaxException"):
        from fairylandfuture.exceptions import database as _db
        return getattr(_db, name)
    if name == "ElasticSearchExecutionException":
        from fairylandfuture.exceptions import elasticsearch as _es
        return getattr(_es, name)
    if name == "FileReadException":
        from fairylandfuture.exceptions import file as _file
        return getattr(_file, name)
    if name in ("ParamsInvalidException", "ParamsTypeException", "ParamsValueException", "ValidationError"):
        from fairylandfuture.exceptions import generic as _gen
        return getattr(_gen, name)
    if name in ("SQLSyntaxExceptMessage", "ElasticSearchExceptMessage"):
        from fairylandfuture.exceptions import messages as _msg
        return getattr(_msg, name)
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
