# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-05-12 22:23:51 UTC+08:00
"""

import abc
from typing import Tuple, NamedTuple, Union, Dict, Any

from fairylandfuture.exceptions.db import SQLSyntaxException
from fairylandfuture.structures.builder.db import FrozenStructureMySQLExecute
from fairylandfuture.structures.builder.db import FrozenStructurePostgreSQLExecute
from fairylandfuture.exceptions.messages.db import SQLSyntaxExceptMessage


class AbstractMySQLOperator(abc.ABC):
    """
    This class is an abstract class for MySQL operations.

    """

    @abc.abstractmethod
    def execute(self, struct: FrozenStructureMySQLExecute, /) -> Union[bool, Tuple[Dict[str, Any], ...]]: ...

    def insert(self, struct: FrozenStructureMySQLExecute, /) -> Union[bool, Tuple[Dict[str, Any], ...]]:
        if not struct.query.lower().startswith("insert"):
            raise SQLSyntaxException(SQLSyntaxExceptMessage.SQL_MUST_INSERT)
        return self.execute(struct)

    def delete(self, struct: FrozenStructureMySQLExecute, /) -> Union[bool, Tuple[Dict[str, Any], ...]]:
        if not struct.query.lower().startswith("delete"):
            raise SQLSyntaxException(SQLSyntaxExceptMessage.SQL_MUST_DELETE)
        return self.execute(struct)

    def update(self, struct: FrozenStructureMySQLExecute, /) -> Union[bool, Tuple[Dict[str, Any], ...]]:
        if not struct.query.lower().startswith("update"):
            raise SQLSyntaxException(SQLSyntaxExceptMessage.SQL_MUST_UPDATE)
        return self.execute(struct)

    @abc.abstractmethod
    def select(self, struct: FrozenStructureMySQLExecute, /) -> Tuple[Dict[str, Any], ...]: ...


class AbstractPostgreSQLOperator(abc.ABC):
    """
    This class is an abstract class for PostgreSQL operations.

    """

    @abc.abstractmethod
    def execute(self, struct: FrozenStructurePostgreSQLExecute, /) -> Union[bool, Tuple[NamedTuple, ...]]: ...

    def insert(self, struct: FrozenStructurePostgreSQLExecute, /) -> Union[bool, Tuple[NamedTuple, ...]]:
        if not struct.query.lower().startswith("insert"):
            raise SQLSyntaxException(SQLSyntaxExceptMessage.SQL_MUST_INSERT)
        return self.execute(struct)

    def delete(self, struct: FrozenStructurePostgreSQLExecute, /) -> Union[bool, Tuple[NamedTuple, ...]]:
        if not struct.query.lower().startswith("delete"):
            raise SQLSyntaxException(SQLSyntaxExceptMessage.SQL_MUST_DELETE)
        return self.execute(struct)

    def update(self, struct: FrozenStructurePostgreSQLExecute, /) -> Union[bool, Tuple[NamedTuple, ...]]:
        if not struct.query.lower().startswith("update"):
            raise SQLSyntaxException(SQLSyntaxExceptMessage.SQL_MUST_UPDATE)
        return self.execute(struct)

    @abc.abstractmethod
    def select(self, struct: FrozenStructurePostgreSQLExecute, /) -> Tuple[NamedTuple, ...]: ...
