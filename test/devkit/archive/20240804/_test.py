# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-08-04 12:35:51 UTC+08:00
"""

from dataclasses import dataclass

from fairylandfuture.modules.db.mysql import MySQLConnector
from fairylandfuture.modules.db.mysql import MySQLOperator
from fairylandfuture.structures.builder.db import FrozenStructureMySQLExecute

from test.utils.logger import journal
from test.devkit import BASE_PATH
from test.devkit import CONFIG


@dataclass(frozen=True)
class Data:
    id: int
    user: str


mysql_config: dict = CONFIG.get("mysql")

journal.info(f"mysql_config: {mysql_config}")

mysql_connector = MySQLConnector(
    mysql_config.get("host"),
    mysql_config.get("port"),
    mysql_config.get("user"),
    mysql_config.get("password"),
    mysql_config.get("database"),
)

connection = MySQLOperator(mysql_connector)

_select_string = "select id, user from users order by id;"
_insert_string = "insert into users (user, email) values (%(user)s, %(email)s);"
_insert_values = {"user": "test", "email": "email@example.com"}

d1 = connection.select(FrozenStructureMySQLExecute(_select_string))
# d2 = connection.insert(StructureMySQLExecute(_insert_string, _insert_values))
# d3 = connection.select(StructureMySQLExecute(_select_string))
journal.info(f"d1: {d1}")
# journal.info(f"d2: {d2}")
# journal.info(f"d3: {d3}")

d3 = tuple(Data(**row) for row in d1)

for r in d3:
    journal.info(f"id: {r.id}, user: {r.user}")
