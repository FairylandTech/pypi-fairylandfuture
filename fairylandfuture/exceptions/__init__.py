# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-08-10 18:26:51 UTC+08:00
"""

from fairylandfuture.exceptions.database import SQLExecutionException, SQLSyntaxException
from fairylandfuture.exceptions.elasticsearch import ElasticSearchExecutionException
from fairylandfuture.exceptions.file import FileReadException
from fairylandfuture.exceptions.generic import (
    ParamsInvalidException,
    ParamsTypeException,
    ParamsValueException,
    ValidationError,
)

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
]
