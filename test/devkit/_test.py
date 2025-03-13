# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-05-12 12:34:53 UTC+08:00
"""

from pathlib import Path


# from test.utils.logger import journal
from test.utils.config import TestConfig

BASE_PATH = Path(__file__).resolve().parent.parent.parent
CONFIG = TestConfig(Path(BASE_PATH, "conf", "dev", "config.yaml")).config


class TestBase:
    @classmethod
    def run(cls):
        """
        This method will run all test methods in the class.
        It will try to catch any exception raised during the test and print it out.

        :return: None
        :rtype: NoneType
        """
        method_list = [func for func in dir(cls) if callable(getattr(cls, func)) and not func.startswith("__")]
        for method in method_list:
            if method.startswith("test_"):
                getattr(cls, method)()
        # journal.success("All tests executed successfully.")


if __name__ == "__main__":
    # journal.info(f"ABS PATH: {BASE_PATH}")
    # journal.debug(f"CONFIG: {CONFIG}")
    TestBase.run()
