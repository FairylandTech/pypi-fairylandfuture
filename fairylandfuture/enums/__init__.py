# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-08-18 00:54:24 UTC+08:00
"""

__all__ = [
    # Datetime
    "DateTimeEnum",
    "TimeZoneEnum",
    # Encode
    "EncodingEnum",
    # File
    "FileModeEnum",
    # Logger
    "LogLevelEnum",
    # HTTP
    "HTTPRequestMethodEnum",
    # Comparison
    "ComparisonOperatorEnum",
]

# Cache for lazy-loaded items
_cache = {}


def __getattr__(name):
    """Lazy import to avoid circular dependencies."""
    global _cache

    if name in _cache:
        return _cache[name]

    if name in ("DateTimeEnum", "TimeZoneEnum"):
        from fairylandfuture.enums import datetime as _dt
        result = getattr(_dt, name)
        _cache[name] = result
        return result
    if name == "EncodingEnum":
        from fairylandfuture.enums.encode import EncodingEnum
        _cache[name] = EncodingEnum
        return EncodingEnum
    if name == "FileModeEnum":
        from fairylandfuture.enums.file import FileModeEnum
        _cache[name] = FileModeEnum
        return FileModeEnum
    if name == "LogLevelEnum":
        from fairylandfuture.enums.logger import LogLevelEnum
        _cache[name] = LogLevelEnum
        return LogLevelEnum
    if name == "HTTPRequestMethodEnum":
        from fairylandfuture.enums import http as _http
        result = getattr(_http, name)
        _cache[name] = result
        return result
    if name == "ComparisonOperatorEnum":
        from fairylandfuture.core.superclass.enumerate import BaseEnum

        class ComparisonOperatorEnum(BaseEnum):
            EQUAL = "="
            NOT_EQUAL = "!="
            GREATER_THAN = ">"
            GREATER_THAN_OR_EQUAL = ">="
            LESS_THAN = "<"
            LESS_THAN_OR_EQUAL = "<="

            IN = "in"
            NOT_IN = "not in"
            LIKE = "like"
            ILIKE = "ilike"
            NOT_LIKE = "not like"
            IS_NULL = "is null"
            IS_NOT_NULL = "is not null"

            @property
            def value(self) -> str:
                return super().value

        _cache[name] = ComparisonOperatorEnum
        return ComparisonOperatorEnum
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
