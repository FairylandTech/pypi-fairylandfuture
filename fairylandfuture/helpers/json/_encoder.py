
# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2025-05-14 10:48:20 UTC+08:00
"""

import json
import datetime
import decimal

from fairylandfuture.enums.chrono import DateTimeEnum

class JsonEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime(DateTimeEnum.DATETIME.value)
        elif isinstance(obj, datetime.date):
            return obj.strftime(DateTimeEnum.DATE.value)
        elif isinstance(obj, datetime.time):
            return obj.strftime(DateTimeEnum.TIME.value)
        elif isinstance(obj, decimal.Decimal):
            return float(obj)

        return super().default(obj)


# class JsonEncoder(JSONEncoder):
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.visited_objects = set()
#
#     def default(self, obj):
#         obj_id = id(obj)
#         if obj_id in self.visited_objects:
#             return "[循环引用]"
#
#         self.visited_objects.add(obj_id)
#
#         try:
#             if isinstance(obj, datetime.datetime):
#                 return obj.strftime(DateTimeEnum.datetime.value)
#             elif isinstance(obj, datetime.date):
#                 return obj.strftime("%Y-%m-%d")
#             elif isinstance(obj, datetime.time):
#                 return obj.strftime("%H:%M:%S")
#             elif isinstance(obj, decimal.Decimal):
#                 return float(obj)
#             else:
#                 return super().default(obj)
#         finally:
#             self.visited_objects.remove(obj_id)