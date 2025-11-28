# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-08-10 18:23:28 UTC+08:00
"""

__all__ = [
    # DateTime
    "DateTimeUtils",
    # Django
    "DjangoRequestUtils",
    # Faker
    "FakeGeneralToolkit",
    "FakeNetworkToolkit",
    "FakeUserToolkit",
    # Net
    "LocalNetworkUtils",
    # Secret
    "CipherUtils",
    "UserPasswordCryptionUtils",
    "PasswordCryptionUtils",
    "Base64Utils",
    # Validator
    "StringValidatorUtils",
]


def __getattr__(name):
    """Lazy import to avoid circular dependencies and optional dependencies."""
    if name == "DateTimeUtils":
        from fairylandfuture.utils._datetime_utils import DateTimeUtils
        return DateTimeUtils
    if name == "DjangoRequestUtils":
        from fairylandfuture.utils.django import DjangoRequestUtils
        return DjangoRequestUtils
    if name in ("FakeGeneralToolkit", "FakeNetworkToolkit", "FakeUserToolkit"):
        from fairylandfuture.utils import faker as _faker
        return getattr(_faker, name)
    if name == "LocalNetworkUtils":
        from fairylandfuture.utils.net import LocalNetworkUtils
        return LocalNetworkUtils
    if name in ("CipherUtils", "UserPasswordCryptionUtils", "PasswordCryptionUtils", "Base64Utils"):
        from fairylandfuture.utils import secret as _secret
        return getattr(_secret, name)
    if name == "StringValidatorUtils":
        from fairylandfuture.utils.validator import StringValidatorUtils
        return StringValidatorUtils
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
