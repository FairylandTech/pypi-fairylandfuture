# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-07-03 22:26:49 UTC+08:00
"""

from fairylandfuture.models.orm.general import BaseModel
from fairylandfuture.models.orm.fields.descriptor import CharField, IntField


class User(BaseModel):
    name = CharField("name", max_length=100)
    age = IntField("age")
    email = CharField("email", max_length=100)

    class Meta:
        table_name = "user"


if __name__ == "__main__":
    user = User(name="alice", age=18)
    user.save()
