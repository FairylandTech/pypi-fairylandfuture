# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2025-11-29 14:03:18 UTC+08:00
"""

import abc

from fairylandfuture.structures.logger import LoggerRecordStructure


class AbstractLoggerAppender(abc.ABC):

    @abc.abstractmethod
    def add_sink(self): ...

    @abc.abstractmethod
    def emit(self, record: LoggerRecordStructure): ...
