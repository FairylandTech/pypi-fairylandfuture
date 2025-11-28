# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-05-18 11:38:39 UTC+08:00
"""

__all__ = [
    # Decorators
    "BaseDecorator",
    "BaseParamsDecorator",
    # Enumerate
    "BaseEnum",
    # Exception
    "BaseProgramException",
    # Faker
    "BaseFaker",
    # File
    "BaseFile",
    "BaseTextFile",
    "BaseYamlFile",
    "BaseJsonFile",
    # Schema
    "PrimitiveSchema",
    "EntitySchema",
    "BaseSchema",
    # Structure
    "BaseStructure",
    "BaseFrozenStructure",
    "BaseStructureTreeNode",
    # Validators
    "Validator",
]


def __getattr__(name):
    """Lazy import to avoid circular dependencies."""
    if name in ("BaseDecorator", "BaseParamsDecorator"):
        from fairylandfuture.core.superclass.decorators import BaseDecorator, BaseParamsDecorator
        return {"BaseDecorator": BaseDecorator, "BaseParamsDecorator": BaseParamsDecorator}[name]
    if name == "BaseEnum":
        from fairylandfuture.core.superclass.enumerate import BaseEnum
        return BaseEnum
    if name == "BaseProgramException":
        from fairylandfuture.core.superclass.exception import BaseProgramException
        return BaseProgramException
    if name == "BaseFaker":
        from fairylandfuture.core.superclass.fakerlib import BaseFaker
        return BaseFaker
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
        from fairylandfuture.core.superclass.validators import Validator
        return Validator
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
