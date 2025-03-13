# coding: utf-8
""" 
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-07-04 12:58:54 UTC+08:00
"""

from fairylandfuture.models.orm.general import BaseModelV2


class TestModel(BaseModelV2):

    def __init__(self, table, columns):
        super().__init__(table, columns)


if __name__ == "__main__":
    test_model = TestModel("test_table", ["id", "name", "age"])
    data = {"id": 1, "name": "John", "age": 20}

    print(test_model.save(data))
    print(test_model.save(data, include_fields=("name", "age")))
    print(test_model.save(data, exclude_fields=("id", "age")))
    print(test_model.save(data, include_fields=("name", "age"), exclude_fields=("id", "age")))

    print(test_model.update({"name": "Jack", "age": 21}, 1))

    print(test_model.list("name=1 and age=20 or name=1 and age=10"))
