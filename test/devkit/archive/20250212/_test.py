# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2025-02-12 20:54:44 UTC+08:00
"""

from fairylandfuture.modules.validator.validators import Validator, RequestValidator
from fairylandfuture.enums.chron import DateTimeEnum
from fairylandfuture.toolkit.utils.chron import DateTimeUtils


def main():
    def validator_date(value: str):
        try:
            _ = DateTimeUtils.datetime_to_timestamp(value, _format=DateTimeEnum.DATE.value)
            return True
        except Exception as err:
            raise err

    # name: str, birthday: yyyy-mm-dd, grade: boolean, score: double
    type_map = {
        "int": int,
        "float": float,
        "double": float,
        "short": int,
        "bool": bool,
        "boolean": bool,
        "str": str
    }

    # 字段名, 类型, 是否必填
    fields_info = [["name", "str", True], ["birthday", "data", True], ["grade", "bool", False], ["score", "double", True]]
    fields_data = {
        "name": "alice",
        "birthday": "2000-01-01",
        # "grade": True,
        "score": 9.0,
    }

    schmea = {}
    for field, typeof, required in fields_info:  # 解包
        if typeof in type_map:
            typedef = type_map.get(typeof)
            validator_factory = None
        elif typeof == "data":
            typedef = str
            validator_factory = validator_date
        else:
            raise RuntimeError

        schmea[field] = Validator(required, typedef, validator_factory)

    valid_data = RequestValidator(schmea).validate(fields_data)

    print(valid_data)


if __name__ == "__main__":
    main()
