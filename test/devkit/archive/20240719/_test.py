# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-07-19 20:27:35 UTC+08:00
"""

from pathlib import Path

from test.utils.config import TestConfig

from fairylandfuture.modules.db.postgresql import PostgreSQLConnector

config = TestConfig(Path(r"/conf/dev/config.yaml")).config.get("postgresql")

host = config.get("host")
port = config.get("port")
user = config.get("user")
password = config.get("password")
database = config.get("database")

connector = PostgreSQLConnector(host=host, port=port, user=user, password=password, database=database)

connector.cursor.execute("SELECT * FROM public_dev_test.author;")
data = connector.cursor.fetchall()
connector.cursor.close()
connector.close()
print(data)
