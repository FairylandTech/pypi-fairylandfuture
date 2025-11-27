# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-09-24 14:41:30 UTC+08:00
"""

from typing import Any

from fairylandfuture.core.superclass.validators import Validator


class ParamsValidator:
    def __init__(self, schema: dict[str, Validator]):
        self.schema = schema

    def validate(self, data: dict[str, Any]) -> dict[str, Any]:
        return {key: validator.validate(data.get(key)) for key, validator in self.schema.items()}
