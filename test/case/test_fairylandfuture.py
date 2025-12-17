# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2025-12-14 16:48:38 UTC+08:00
"""

import unittest

from fairylandlogger.logger import LogManager

from fairylandfuture.utils import DateTimeUtils


class TestFairylandFuture(unittest.IsolatedAsyncioTestCase):

    def setUp(self):
        super().setUp()

    def tearDown(self):
        LogManager.reset()

    async def test_logger_basic(self):
        api_logger = LogManager.get_logger("api", "service/api")
        api_logger.debug("Debug message from API logger")
        api_logger.info("Info message from API logger")
        api_logger.warning("Warning message from API logger")
        api_logger.error("Error message from API logger")
        api_logger.critical("Critical message from API logger")
        api_logger.success("Success message from API logger")

        service_logger = LogManager.get_logger("service", "service/main")
        service_logger.debug("Debug message from Service logger")
        service_logger.info("Info message from Service logger")
        service_logger.warning("Warning message from Service logger")
        service_logger.error("Error message from Service logger")
        service_logger.critical("Critical message from Service logger")
        service_logger.success("Success message from Service logger")

        service_logger.info(f"Current UTC time: {DateTimeUtils.unzone_utc()}")


if __name__ == "__main__":
    unittest.main()
