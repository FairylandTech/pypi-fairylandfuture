# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2025-01-22 14:39:17 UTC+08:00
"""

from fairylandfuture.modules.validator.validators import Validator, RequestValidator


data = {"id": 1, "name": "name"}
validator_schema = {
    "id": Validator(required=True, typedef=int),
    "name": Validator(required=True, typedef=str),
}

result = RequestValidator(validator_schema).validate(data)

print(result)
