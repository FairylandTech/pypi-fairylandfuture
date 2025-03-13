# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-05-13 13:23:18 UTC+08:00
"""

from typing import Any, Dict, List, Tuple, Union

import pymysql
from _test import TestBase

# from fairylandfuture.modules.datasource import MySQLDatabase


def handle_connection(func):
    def wrapper(self, *args, **kwargs):
        self.conn = pymysql.connect(host=self.host, port=self.port, user=self.user, password=self.password, database=self.database)
        self.cur = self.conn.cursor()
        try:
            result = func(self, *args, **kwargs)
            self.conn.commit()
            return result
        except Exception as err:
            self.conn.rollback()
            raise err
        finally:
            if self.cur:
                self.cur.close()
            if self.conn:
                self.conn.close()

    return wrapper


class MySQLDataSource:

    def __init__(self, host: str, port: int, user: str, password: str, database: str):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database

    def execute(self, sql: str, params: Union[Tuple[Any, ...], Dict[str, Any], None] = None) -> bool:
        self.cur.execute(sql, params)
        return True

    @handle_connection
    def execute_set(self, mapping_data: Dict[str, Union[Tuple[Any, ...], Dict[str, Any]]]) -> bool:
        for sql, params in mapping_data.items():
            self.cur.execute(sql, params)
        return True

    @handle_connection
    def insert(self, sql: str, params: Union[Tuple[Any, ...], Dict[str, Any], None] = None) -> bool:
        return self.execute(sql, params)

    @handle_connection
    def insertmany(self, sql: str, paramset: Union[Tuple[Tuple[Any, ...], ...], Tuple[Dict[str, Any], ...]]) -> bool:
        self.cur.executemany(sql, paramset)
        return True

    @handle_connection
    def delete(self, sql: str, params: Union[Tuple[Any, ...], Dict[str, Any], None] = None) -> bool:
        return self.execute(sql, params)

    @handle_connection
    def select(self, sql: str, params: Union[Tuple[Any, ...], Dict[str, Any], None] = None) -> Union[Tuple[Tuple[Any, ...], ...], List[List[Any]]]:
        self.cur.execute(sql, params)
        results = self.cur.fetchall()
        return results

    @handle_connection
    def update(self, sql: str, params: Union[Tuple[Any, ...], Dict[str, Any], None] = None) -> bool:
        return self.execute(sql, params)


class TestMySQLDataSource(TestBase):

    @classmethod
    def test_mysql(cls):
        ds = MySQLDataSource(_HOST, _PORT, _USER, _PASSWORD, _DATABASE)
        # sql = "select * from public_db_test.tb_test;"
        sql1 = (
            "select public_db_test.tb_test.id, "
            "public_db_test.tb_test.name, "
            "date_format(public_db_test.tb_test.create_time, '%Y-%m-%d %H:%i:%s') as create_time "
            "from public_db_test.tb_test;"
        )

        update_sql1 = "update public_db_test.tb_test " "set status = 0 " "where id = %(id)s;"
        update_sql2 = "update public_db_test.tb_test " "set status = 1 " "where id = %(id)s;"
        # a = ds.select(sql1)
        # print(a)
        mapping_data = {update_sql1: {"id": 1}, update_sql2: {"id": 20}}
        ds.execute_set(mapping_data=mapping_data)


if __name__ == "__main__":
    TestMySQLDataSource.run()
