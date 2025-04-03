# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-06-28 23:13:08 UTC+08:00
"""

from typing import Dict, Any
from pathlib import Path

from fairylandfuture.modules.journal import journal
from fairylandfuture.modules.db.mysql import MySQLDatabase, MySQLConnector
from fairylandfuture.utils.builder.expression import QueryMySQLBuilder, InsertMySQLBuilder
from fairylandfuture.structures.builder.db import MySQLExecuteFrozenStructure, StructureSQLInsertManyParams

from test.utils.config import TestConfig

config: Dict[str, Any] = TestConfig(Path(r"C:\Lionel\Project\Github\PrettiestFairy\pypi-fairylandfuture\conf\dev\config.yaml")).config.get("mysql")

host = config.get("host")
port = config.get("port")
user = config.get("user")
password = config.get("password")
database = config.get("database")
table = "users"

datasource = MySQLDatabase(host=host, port=port, user=user, password=password, database=database)
print("第一次查询".center(50, "="))
query_params = MySQLExecuteFrozenStructure(QueryMySQLBuilder(table).to_string())
print(f"SQL: {query_params.expression}, Params: {query_params.params}")
data = datasource.select(query_params)
print(f"Results: {data}")
# insert_params = StructureSQLExecuteParams(InsertMySQLBuilder(table, ("user", "email")).to_string(), {"user": "李四", "email": "lisi@example.com"})
# print(f"SQL: {insert_params.expression}, Params: {insert_params.params}")
# datasource.insert(insert_params)
print("批量插入".center(50, "="))
muilt_insert_params = StructureSQLInsertManyParams(
    InsertMySQLBuilder(table, ("user", "email")).to_string(),
    ({"user": "王五", "email": "wangwu@example.com"}, {"user": "赵六", "email": "zhaoliu@exmaple.com"}),
)
datasource.insertmany(muilt_insert_params)
print("第二次查询".center(50, "="))
query_params = MySQLExecuteFrozenStructure(QueryMySQLBuilder(table).to_string())
print(f"SQL: {query_params.expression}, Params: {query_params.params}")
data = datasource.select(query_params)
print(f"Results: {data}")
