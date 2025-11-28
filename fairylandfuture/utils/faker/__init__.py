# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-10-15 16:05:21 UTC+08:00
"""

__all__ = [
    "FakeGeneralToolkit",
    "FakeNetworkToolkit",
    "FakeUserToolkit",
]


def __getattr__(name):
    """Lazy import to avoid loading faker modules unless needed."""
    if name == "FakeGeneralToolkit":
        from fairylandfuture.utils.faker.generic import FakeGeneralToolkit
        return FakeGeneralToolkit
    if name == "FakeNetworkToolkit":
        from fairylandfuture.utils.faker.network import FakeNetworkToolkit
        return FakeNetworkToolkit
    if name == "FakeUserToolkit":
        from fairylandfuture.utils.faker.user import FakeUserToolkit
        return FakeUserToolkit
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
