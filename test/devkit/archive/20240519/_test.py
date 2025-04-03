# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-05-19 11:26:00 UTC+08:00
"""

from datetime import datetime
from typing import Any, Dict

import yaml

from bin.generic import DEV_CASE_CONFIG_FILE_PATH
from fairylandfuture.enums.chrono import DateTimeEnum, EncodingEnum
from fairylandfuture.structures.builder.db import MySQLExecuteFrozenStructure, StructureSQLInsertManyParams
from fairylandfuture.modules.datasource import MySQLDataSource

with open(DEV_CASE_CONFIG_FILE_PATH, encoding=EncodingEnum.utf8.value) as stream:
    case_conf: Dict[str, Dict[str, Any]] = yaml.safe_load(stream)

MYSQL_CONFIG = case_conf.get("mysql")

datasource = MySQLDataSource(
    MYSQL_CONFIG.get("host"),
    MYSQL_CONFIG.get("port"),
    MYSQL_CONFIG.get("username"),
    MYSQL_CONFIG.get("password"),
    MYSQL_CONFIG.get("database"),
)

query_now = ExecuteParams("select now() as now;")

add_col_sql = "alter table tb_test " "add age int  default 0 not null;"
update_age = "update tb_test " "set age = 18 " "where id = %(id)s"

query_name = "select id, name, age " "from tb_test " "where id = %(id)s;"

instermany = "insert into tb_test (name, age) " "values (%(name)s, %(age)s) ;"

instermany_v = ({"name": "郭昕蕊", "age": 51}, {"name": "董敏", "age": 21})

query_now_result = datasource.select(query_now)
now: datetime = query_now_result.get("now")
print(now.strftime(DateTimeEnum.datetime_cn))

multiple_exec = (ExecuteParams(add_col_sql), ExecuteParams(update_age, {"id": 1}))

# print(datasource.multiple(multiple_exec))

datasource.insertmany(InsertManyParams(instermany, instermany_v))
