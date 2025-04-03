# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2025-04-01 14:18:22 UTC+08:00
"""

from datetime import datetime
from typing import Sequence, Mapping
from fairylandfuture.core.superclass.structures.structure import BaseStructure, BaseFrozenStructure, BaseStructureTreeNode


class SerializableKit(object):

    @classmethod
    def serialize(cls, obj):
        if hasattr(obj, "asdict"):
            return obj.asdict
        elif isinstance(obj, Sequence):
            return [cls.serialize(item) for item in obj]
        elif isinstance(obj, Mapping):
            return {key: cls.serialize(value) for key, value in obj.items()}
        elif isinstance(obj, datetime):
            return obj.isoformat(sep=" ", timespec="seconds")
        elif isinstance(obj, (BaseStructure, BaseFrozenStructure, BaseStructureTreeNode)):
            return obj.to_dict()
        else:
            return obj
