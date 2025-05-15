# coding: utf-8
""" 
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-07-05 12:43:37 UTC+08:00
"""

from typing import Dict, Any, List, NamedTuple
from pathlib import Path

from test.utils.config import TestConfig
from fairylandfuture.database import PostgreSQLConnector


class SQLData(NamedTuple):
    feature_id: str
    feature_name: str
    sub_feature_id: str
    sub_feature_name: str
    is_supported: str
    is_verified_by: str
    comments: str


config: Dict[str, Any] = TestConfig(Path(r"C:\Lionel\Project\Github\pypi-fairylandfuture\conf\dev\config.yaml")).config.get("postgresql")
print(repr(config))

pg = PostgreSQLConnector(
    host=config.get("host"),
    port=config.get("port"),
    user=config.get("user"),
    password=config.get("password"),
    database=config.get("database"),
    schema="information_schema",
)

pg.cursor.execute("select * from sql_features limit 10 offset 0;")
data: List[SQLData] = pg.cursor.fetchall()
pg.cursor.close()
for i in data:
    print(i, i.feature_id)
# pg.reconnect()
# pg.cursor.execute("select * from information_schema.sql_features limit 10 offset 10;")
# data2 = pg.cursor.fetchall()
# pg.cursor.close()
# pg.close()


from collections import namedtuple

column_name = ["a", "b", "c"]
row_1_data = [1, 2, 3]
row_2_data = [1, 2, 3]

a = map(lambda x: namedtuple("Data", column_name)(*x), (row_1_data, row_2_data))
for i in a:
    print(i, i.a, i.b, i.c)

print(pg.dsn.__repr__())
