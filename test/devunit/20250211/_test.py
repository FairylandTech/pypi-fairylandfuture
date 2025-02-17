# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2025-02-11 14:14:02 UTC+08:00
"""

from fairylandfuture.modules.db.postgresql import PostgreSQLConnector
from fairylandfuture.modules.db.postgresql import PostgreSQLOperation
from fairylandfuture.structures.builder.db import StructurePostgreSQLExecute


def main():
    connector = PostgreSQLConnector(
        host="10.65.66.155",
        port=5432,
        user="nsc",
        password="6#YcGei@!v7",
        database="nsc"
    )

    operation = PostgreSQLOperation(connector)

    sql = "select id, name from internal_app_test.test_table;"
    result = operation.select(StructurePostgreSQLExecute(sql))



if __name__ == '__main__':
    main()
