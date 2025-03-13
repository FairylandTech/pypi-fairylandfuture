# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-09-26 13:26:19 UTC+08:00
"""

from loguru import logger

from fairylandfuture.modules.journal import Journal

if __name__ == "__main__":
    logger.info("123")
    journal = Journal(debug=True, serialize=True, console=True)
    journal.info("123")
    logger.info("456")
