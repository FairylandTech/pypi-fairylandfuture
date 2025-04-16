# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2025-04-16 14:07:09 UTC+08:00
"""

import dotenv


class Configure:

    class DotEnv:

        @classmethod
        def load(cls, path: str) -> None:
            """
            加载 .env 文件

            :param path: .env 文件路径
            :type path: str
            """
            dotenv.load_dotenv(path)
