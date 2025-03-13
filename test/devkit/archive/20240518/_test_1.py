# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-05-18 19:21:31 UTC+08:00
"""

from fairylandfuture.modules.datasource import MySQLDataSource

mysql = MySQLDataSource(_HOST, _PORT, _USER, _PASSWORD, _DATABASE)

print(mysql.select("select now();"))
