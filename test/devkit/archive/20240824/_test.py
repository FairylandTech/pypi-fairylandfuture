# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-08-24 16:05:40 UTC+08:00
"""

from fairylandfuture.structures.builder.db import MySQLExecuteFrozenStructure, PostgreSQLExecuteFrozenStructure
from fairylandfuture.tools.databases.mysql import MySQLSQLSimpleConnectionPool
from fairylandfuture.tools.databases.postgresql import PostgreSQLSimpleConnectionPool
from test.devkit import CONFIG
from test.utils.logger import journal

mysql_config: dict = CONFIG.get("mysql")
pg_config: dict = CONFIG.get("postgresql")

journal.info(f"mysql_config: {mysql_config}")

pool = MySQLSQLSimpleConnectionPool(
    mysql_config.get("host"),
    mysql_config.get("port"),
    mysql_config.get("user"),
    mysql_config.get("password"),
    mysql_config.get("database"),
)

sql = "SELECT * FROM users;"
a = pool.execute(MySQLExecuteFrozenStructure(sql))
print(a)

pg_pool = PostgreSQLSimpleConnectionPool(
    pg_config.get("host"),
    pg_config.get("port"),
    pg_config.get("user"),
    pg_config.get("password"),
    pg_config.get("database"),
)

pg_sql = "SELECT * FROM public_dev_test.publish;"
b = pg_pool.execute(PostgreSQLExecuteFrozenStructure(pg_sql))
print(b)
