# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2025-05-14 10:48:20 UTC+08:00
"""

import datetime
import decimal
import json

from fairylandfuture.core.superclass.structure import BaseFrozenStructure, BaseStructure
from fairylandfuture.enums.chron import DateTimeEnum


class JsonEncoder(json.JSONEncoder):

    def default(self, o):
        if isinstance(o, datetime.datetime):
            return o.strftime(DateTimeEnum.DATETIME.value)
        elif isinstance(o, datetime.date):
            return o.strftime(DateTimeEnum.DATE.value)
        elif isinstance(o, datetime.time):
            return o.strftime(DateTimeEnum.TIME.value)
        elif isinstance(o, decimal.Decimal):
            return float(o)
        elif isinstance(o, (BaseStructure, BaseFrozenStructure)):
            return o.to_json()

        return super().default(o)
