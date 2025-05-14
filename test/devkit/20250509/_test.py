# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2025-05-09 00:18:13 UTC+08:00
"""

import pprint
from enum import Enum, StrEnum
from datetime import datetime

from fairylandfuture.helpers.json.serializer import JsonSerializerHelper

def main():
    data = {
        "name": "示例数据",
        "created_at": datetime.now(),
        "items": [
            {"id": 1, "updated_at": datetime(2025, 5, 14, 10, 30, 0)},
            {"id": 2, "updated_at": datetime(2025, 5, 15, 14, 45, 0)}
        ]
    }

    print(JsonSerializerHelper.serialize(data))


if __name__ == "__main__":
    main()
