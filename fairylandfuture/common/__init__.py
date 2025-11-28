# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-05-09 18:43:58 UTC+08:00
"""

# Lazy imports to avoid circular dependencies
__all__ = [
    # File
    "File",
    "TextFile",
    "YamlFile",
    "JsonFile",
    "OtherTextFile",
    # Request
    "HTTPSimpleRequest",
    # Validator
    "ParamsValidator",
]


def __getattr__(name):
    """Lazy import to avoid circular dependencies."""
    if name in ("File", "TextFile", "YamlFile", "JsonFile", "OtherTextFile"):
        from fairylandfuture.common import file as _file
        return getattr(_file, name)
    if name == "HTTPSimpleRequest":
        from fairylandfuture.common import request as _request
        return getattr(_request, name)
    if name == "ParamsValidator":
        from fairylandfuture.common.validator import ParamsValidator
        return ParamsValidator
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
