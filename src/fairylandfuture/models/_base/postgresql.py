# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2025-12-31 01:27:05 UTC+08:00
"""

import typing as t

from sqlalchemy.orm import declared_attr

from . import BaseModel


class BaseModelPostgreSQL(BaseModel):
    __abstract__ = True
    __table_schema__ = "public"

    @classmethod
    @declared_attr
    def __table_args__(cls) -> t.Dict[str, str]:
        return {"schema": cls.__table_schema__}
