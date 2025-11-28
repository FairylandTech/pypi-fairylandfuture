# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-05-09 18:43:27 UTC+08:00
"""

__all__ = [
    # Metaclass
    "SingletonMeta",
    # Superclass
    "BaseDecorator",
    "BaseParamsDecorator",
    "BaseEnum",
    "BaseProgramException",
    "BaseFaker",
    "BaseFile",
    "BaseTextFile",
    "BaseYamlFile",
    "BaseJsonFile",
    "PrimitiveSchema",
    "EntitySchema",
    "BaseSchema",
    "BaseStructure",
    "BaseFrozenStructure",
    "BaseStructureTreeNode",
    "Validator",
]


def __getattr__(name):
    """Lazy import to avoid circular dependencies."""
    if name == "SingletonMeta":
        from fairylandfuture.core.metaclass import SingletonMeta
        return SingletonMeta
    if name in ("BaseDecorator", "BaseParamsDecorator"):
        from fairylandfuture.core.superclass import decorators as _dec
        return getattr(_dec, name)
    if name == "BaseEnum":
        from fairylandfuture.core.superclass import enumerate as _enum
        return getattr(_enum, name)
    if name == "BaseProgramException":
        from fairylandfuture.core.superclass import exception as _exc
        return getattr(_exc, name)
    if name == "BaseFaker":
        from fairylandfuture.core.superclass import fakerlib as _faker
        return getattr(_faker, name)
    if name in ("BaseFile", "BaseTextFile", "BaseYamlFile", "BaseJsonFile"):
        from fairylandfuture.core.superclass import file as _file
        return getattr(_file, name)
    if name in ("PrimitiveSchema", "EntitySchema", "BaseSchema"):
        from fairylandfuture.core.superclass import schema as _schema
        return getattr(_schema, name)
    if name in ("BaseStructure", "BaseFrozenStructure", "BaseStructureTreeNode"):
        from fairylandfuture.core.superclass import structure as _struct
        return getattr(_struct, name)
    if name == "Validator":
        from fairylandfuture.core.superclass import validators as _val
        return getattr(_val, name)
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
