# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-05-12 22:23:51 UTC+08:00
"""

import abc
from typing import Tuple, NamedTuple, Union, Dict, Any

from fairylandfuture.exceptions.databases import SQLSyntaxException
from fairylandfuture.structures.builder.databases import StructureMySQLExecute
from fairylandfuture.structures.builder.databases import StructurePostgreSQLExecute


class AbstractMySQLOperation(abc.ABC):
    """
    This class is an abstract class for MySQL operations.

    """

    @abc.abstractmethod
    def execute(self, struct: StructureMySQLExecute, /) -> Union[bool, Tuple[Dict[str, Any], ...]]: ...

    def insert(self, struct: StructureMySQLExecute, /) -> Union[bool, Tuple[Dict[str, Any], ...]]:
        if not struct.query.lower().startswith("insert"):
            raise SQLSyntaxException("SQL syntax error. The query must be an insert statement.")
        return self.execute(struct)

    def delete(self, struct: StructureMySQLExecute, /) -> Union[bool, Tuple[Dict[str, Any], ...]]:
        if not struct.query.lower().startswith("delete"):
            raise SQLSyntaxException("SQL syntax error. The query must be a delete statement.")
        return self.execute(struct)

    def update(self, struct: StructureMySQLExecute, /) -> Union[bool, Tuple[Dict[str, Any], ...]]:
        if not struct.query.lower().startswith("update"):
            raise SQLSyntaxException("SQL syntax error. The query must be an update statement.")
        return self.execute(struct)

    @abc.abstractmethod
    def select(self, struct: StructureMySQLExecute, /) -> Tuple[Dict[str, Any], ...]: ...


class AbstractPostgreSQLOperation(abc.ABC):
    """
    This class is an abstract class for PostgreSQL operations.

    """

    @abc.abstractmethod
    def execute(self, struct: StructurePostgreSQLExecute, /) -> Union[bool, Tuple[NamedTuple, ...]]: ...

    def insert(self, struct: StructurePostgreSQLExecute, /) -> Union[bool, Tuple[NamedTuple, ...]]:
        if not struct.query.lower().startswith("insert"):
            raise SQLSyntaxException("SQL syntax error. The query must be an insert statement.")
        return self.execute(struct)

    def delete(self, struct: StructurePostgreSQLExecute, /) -> Union[bool, Tuple[NamedTuple, ...]]:
        if not struct.query.lower().startswith("delete"):
            raise SQLSyntaxException("SQL syntax error. The query must be a delete statement.")
        return self.execute(struct)

    def update(self, struct: StructurePostgreSQLExecute, /) -> Union[bool, Tuple[NamedTuple, ...]]:
        if not struct.query.lower().startswith("update"):
            raise SQLSyntaxException("SQL syntax error. The query must be an update statement.")
        return self.execute(struct)

    @abc.abstractmethod
    def select(self, struct: StructurePostgreSQLExecute, /) -> Tuple[NamedTuple, ...]: ...
