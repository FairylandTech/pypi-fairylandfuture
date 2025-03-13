# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-06-24 12:31:33 UTC+08:00
"""

import os.path

from fairylandfuture.modules.datasource import MySQLConnector

from test.utils.config import TestConfig
from test.devkit._test import BASE_PATH
from bin.generic import DEV_CONFIG_FILE_PATH

if __name__ == "__main__":
    config_instance = TestConfig(DEV_CONFIG_FILE_PATH)
    config = config_instance.config
    mysql_config = config.get("mysql")

    connection = MySQLConnector(
        mysql_config.get("host"),
        mysql_config.get("port"),
        mysql_config.get("user"),
        mysql_config.get("password"),
        mysql_config.get("database"),
    )

    print(connection.host)
    print(connection.post)
    print(connection.user)
    print(connection.database)

    connect = connection.__connect()
    cursor = connect.cursor()

    cursor.execute("select mysql.user.host, mysql.user.user from mysql.user;")
    data = cursor.fetchall()
    print(data)
    cursor.close()
    connect.close()
