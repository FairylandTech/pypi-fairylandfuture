# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-05-18 18:44:08 UTC+08:00
"""

import typing as t

from sqlalchemy import Column, Integer, inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped

from fairylandfuture.core.superclass.schema import BaseSchema

Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True

    id: Mapped[int] = Column(Integer, primary_key=True, autoincrement=True, comment="ID")

    @classmethod
    def from_schema(cls, schema: BaseSchema):
        ins = cls()
        for field, value in schema.to_dict().items():
            if hasattr(ins, field):
                setattr(ins, field, value)
        return ins

    def to_dict(self) -> dict[str, t.Any]:
        return {field.name: getattr(self, field.name) for field in inspect(self.__class__).columns}
