# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2025-11-25 12:25:58 UTC+08:00
"""

import unittest

import psycopg.sql

from fairylandfuture.const.database import SQLKeywordConst
from fairylandfuture.core.metaclass.singleton import SingletonMeta
from test import TestBase


class A(metaclass=SingletonMeta):

    def __init__(self):
        self.name = "Singleton A"


class Test(TestBase):

    def test_singleton(self):
        a1 = A()
        a2 = A()
        self.assertIs(a1, a2)
        print(f"a1 id: {id(a1)}, a2 id: {id(a2)}")

    def test_pgsql(self):
        data = {
            "name": "Alex",
        }

        columns = list(data.keys())

        table_identifier = psycopg.sql.Identifier("movie", "tb_virtual")
        execute_sql = psycopg.sql.SQL("{insert} {table} ({fields}) {values} ({placeholders});").format(
            insert=SQLKeywordConst.PostgreSQL.INSERT_INTO,
            table=table_identifier,
            fields=psycopg.sql.SQL(", ").join(map(psycopg.sql.Identifier, columns)),
            values=SQLKeywordConst.PostgreSQL.VALUES,
            placeholders=psycopg.sql.SQL(", ").join(psycopg.sql.Placeholder(column) for column in columns),
        )

        print(execute_sql.as_string())


if __name__ == "__main__":
    unittest.main()
