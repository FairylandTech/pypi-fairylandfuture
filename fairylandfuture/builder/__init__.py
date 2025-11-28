# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2025-11-28 12:26:30 UTC+08:00
"""

__all__ = [
    "TreeBuilderToolkit",
    "TreeBuilderToolkitV2",
]


def __getattr__(name):
    """Lazy import to avoid circular dependencies."""
    if name in ("TreeBuilderToolkit", "TreeBuilderToolkitV2"):
        from fairylandfuture.builder.tree import TreeBuilderToolkit, TreeBuilderToolkitV2
        return {"TreeBuilderToolkit": TreeBuilderToolkit, "TreeBuilderToolkitV2": TreeBuilderToolkitV2}[name]
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
