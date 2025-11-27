# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2025-05-14 10:48:20 UTC+08:00
"""

import json
import typing as t

from fairylandfuture.helpers.json.encoder import JsonEncoder

ClazzType = t.TypeVar("ClazzType")
StrAny = t.TypeVar("StrAny", str, bytes, bytearray)


class JsonSerializerHelper:

    @classmethod
    def serialize(cls, value):
        return json.dumps(value, cls=JsonEncoder, ensure_ascii=False, sort_keys=True, separators=(",", ":"))

    @classmethod
    def deserialize(cls, value: StrAny | dict[str, t.Any], clazz: t.Callable[..., ClazzType] | None = None) -> ClazzType:
        if isinstance(value, dict):
            if not clazz:
                return value

            return clazz(**value)

        if not clazz:
            return json.loads(value)

        return json.loads(value, object_hook=lambda x: clazz(**x))
