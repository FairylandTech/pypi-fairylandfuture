# coding: utf-8
""" 
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-06-29 14:54:28 UTC+08:00
"""

from typing import Dict, Any
from pathlib import Path

from fairylandfuture.modules.db.mysql import MySQLOperator, MySQLConnector
from fairylandfuture.structures.builder.db import MySQLExecuteFrozenStructure

from test.utils.config import TestConfig
from test.utils.logger import journal

# config: Dict[str, Any] = TestConfig(Path(r"C:\Lionel\Project\Github\pypi-fairylandfuture\conf\dev\config.yaml")).config.get("mysql")
config: Dict[str, Any] = TestConfig(Path(r"C:\Lionel\Project\Github\PrettiestFairy\pypi-fairylandfuture\conf\dev\config.yaml")).config.get("mysql")

host = config.get("host")
port = config.get("port")
user = config.get("user")
password = config.get("password")
database = config.get("database")
table = "users"

datasource = MySQLOperator(MySQLConnector(host=host, port=port, user=user, password=password, database=database))
print("第一次查询".center(50, "="))
query_1 = MySQLExecuteFrozenStructure("select * from users;")
print(f"SQL: {query_1.query}, Params: {query_1.args}")
data = datasource.select(query_1)
print(f"Results: {data}")
print("第一次查询成功".center(50, "="))

insert_sql = MySQLExecuteFrozenStructure("insert into users (user, email) values (%(user)s, %(email)s);", {"user": "Lionel", "email": "email@example.com"})
print("第一次插入".center(50, "="))
print(f"SQL: {insert_sql.query}, Params: {insert_sql.args}")
data = datasource.execute(insert_sql)
print(f"Results: {data}")
print("第一次插入成功".center(50, "="))

print("第二次查询".center(50, "="))
query_2 = MySQLExecuteFrozenStructure("select * from users;")
print(f"SQL: {query_2.query}, Params: {query_2.args}")
data = datasource.select(query_2)
print(f"Results: {data}")
print("第二次查询成功".center(50, "="))
