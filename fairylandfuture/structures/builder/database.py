# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-06-27 00:07:43 UTC+08:00
"""

from collections.abc import Mapping, MutableMapping, MutableSequence, Sequence
from dataclasses import dataclass, field

from fairylandfuture.core.superclass.structure import BaseFrozenStructure


@dataclass(frozen=True)
class MySQLExecuteFrozenStructure(BaseFrozenStructure):
    query: str
    args: Sequence | MutableSequence | Mapping | MutableMapping | None = field(default=None)


@dataclass(frozen=True)
class PostgreSQLExecuteFrozenStructure(BaseFrozenStructure):
    query: str
    vars: Sequence | MutableSequence | Mapping | MutableMapping | None = field(default=None)
