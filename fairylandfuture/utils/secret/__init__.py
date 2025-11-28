# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-06-14 18:08:15 UTC+08:00
"""

__all__ = [
    "CipherUtils",
    "UserPasswordCryptionUtils",
    "PasswordCryptionUtils",
    "Base64Utils",
]


def __getattr__(name):
    """Lazy import."""
    if name in ("CipherUtils", "UserPasswordCryptionUtils", "PasswordCryptionUtils"):
        from fairylandfuture.utils.secret import cipher as _cipher
        return getattr(_cipher, name)
    if name == "Base64Utils":
        from fairylandfuture.utils.secret.encoder import Base64Utils
        return Base64Utils
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
