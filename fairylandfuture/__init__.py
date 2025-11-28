# coding: UTF-8
"""
FairylandFuture - A comprehensive Python utility library.

@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-05-09 16:15:43 UTC+08:00

Usage examples:
    # Core imports
    from fairylandfuture.core import SingletonMeta, BaseEnum, BaseProgramException
    from fairylandfuture.core.metaclass import SingletonMeta
    from fairylandfuture.core.superclass import BaseEnum, BaseSchema, BaseStructure

    # Enum imports
    from fairylandfuture.enums import DateTimeEnum, EncodingEnum, LogLevelEnum

    # Exception imports
    from fairylandfuture.exceptions import SQLSyntaxException, ValidationError

    # Database imports
    from fairylandfuture.database import MySQLConnector, MySQLOperator, PostgreSQLConnector

    # Toolkit imports
    from fairylandfuture.toolkit import Journal, DateTimeToolkit
    from fairylandfuture.toolkit.journal import Journal
    from fairylandfuture.toolkit.utils.chron import DateTimeToolkit
    from fairylandfuture.toolkit.utils.encryption import CipherToolkit

    # Structure imports
    from fairylandfuture.structures import ResponseStructure, MySQLExecuteFrozenStructure

    # Helper imports
    from fairylandfuture.helpers import JsonSerializerHelper
    from fairylandfuture.helpers.json import JsonEncoder, JsonSerializerHelper

    # Model imports
    from fairylandfuture.models import BaseModel

    # Interface imports
    from fairylandfuture.interface import DRFResponseMixin
"""

__version__ = "1.3.3"
__author__ = "Lionel Johnson"
__email__ = "fairylandfuture@outlook.com"

__all__ = [
    "__version__",
    "__author__",
    "__email__",
]