# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2025-11-24 21:16:30 UTC+08:00
"""

import time
import typing as t
import unittest
from dataclasses import dataclass
import datetime as dt
from enum import auto

from sqlalchemy import Column, String, DateTime, Boolean, Integer, ForeignKey
from sqlalchemy.orm import relationship, Mapped

from fairylandfuture.core.superclass.enumerate import BaseEnum
from fairylandfuture.core.superclass.schema import BaseSchema
from fairylandfuture.core.superclass.structure import BaseStructure, BaseFrozenStructure
from fairylandfuture.helpers.json.serializer import JsonSerializerHelper
from fairylandfuture.models import BaseModel
from test import TestBase


@dataclass
class TestJsonEntity(BaseStructure):
    id: int
    name: str
    value: t.Optional[float] = None


@dataclass
class TestJsonEntityDict(BaseStructure):
    id: int
    eneity: TestJsonEntity


class TestJsonEntity2:

    def __init__(self, id: int, name: str, value: t.Optional[float] = None) -> None:
        self.id = id
        self.name = name
        self.value = value

    def __repr__(self):
        return f"TestJsonEntity2(id={self.id}, name={self.name}, value={self.value})"


class TestJsonEntity3:
    id: int
    name: str
    value: t.Optional[float] = None

    @classmethod
    def build(cls, id: int, name: str, value: t.Optional[float] = None) -> "TestJsonEntity3":
        instance = cls()
        instance.id = id
        instance.name = name
        instance.value = value
        return instance

    def __repr__(self):
        return f"TestJsonEntity3(id={self.id}, name={self.name}, value={self.value})"


class UserRuleEnum(BaseEnum):
    DEFAULT = auto()
    ADMIN = "admin"
    USER = "user"


class UserDTO(BaseSchema):
    id: t.Optional[int] = None
    name: str
    email: str
    user_rule: UserRuleEnum
    # address_id: t.Optional[int] = None


class UserAddressEntity(BaseModel):
    __tablename__ = "address"

    address: Mapped[str] = Column(String(200), nullable=False)
    created_at: Mapped[dt.datetime] = Column(DateTime, default=dt.datetime.now)
    updated_at: Mapped[dt.datetime] = Column(DateTime, default=dt.datetime.now, onupdate=dt.datetime.now)
    existed: Mapped[bool] = Column(Boolean, default=True)

    user: Mapped[t.Optional["UserEntity"]] = relationship("UserEntity", back_populates="address")

    def __repr__(self):
        return f"<UserAddressEntity(id={self.id}, address={self.address}, created_at={self.created_at}, updated_at={self.updated_at}, existed={self.existed}>"


class UserEntity(BaseModel):
    __tablename__ = "user"

    name: Mapped[str] = Column(String(50), unique=True, nullable=False)
    email: Mapped[str] = Column(String(100), nullable=False)
    user_rule: Mapped[str] = Column(String(20), nullable=False)
    address_id: Mapped[int] = Column(Integer, ForeignKey("address.id"))
    created_at: Mapped[dt.datetime] = Column(DateTime, default=dt.datetime.now)
    updated_at: Mapped[dt.datetime] = Column(DateTime, default=dt.datetime.now, onupdate=dt.datetime.now)
    existed: Mapped[bool] = Column(Boolean, default=True)

    address: Mapped[t.Optional["UserAddressEntity"]] = relationship("UserAddressEntity", back_populates="user")

    def __repr__(self):
        return f"<UserEntity(id={self.id}, name={self.name}, email={self.email}, user_rule={self.user_rule}, address_id={self.address_id},created_at={self.created_at}, updated_at={self.updated_at}, existed={self.existed}>"


@dataclass(frozen=True)
class UserVO(BaseFrozenStructure):
    id: int
    name: str
    email: str
    updated_at: t.Optional[dt.datetime] = None


class JsonSerializerHelperTestCase(TestBase):

    def test_entity1(self):
        entity: TestJsonEntity = TestJsonEntity(id=1, name="Test", value=10.5)
        entity_serialized = JsonSerializerHelper.serialize(entity)
        print("eneity 1 serializer:", entity_serialized)
        self.assertIsInstance(entity_serialized, str)

        entity_deserialized: TestJsonEntity = JsonSerializerHelper.deserialize(entity_serialized, TestJsonEntity)
        print("eneity 1 deserializer:", entity_deserialized)
        self.assertIsInstance(entity_deserialized, TestJsonEntity)

        entity_deserialized2_dict: t.Dict[str, t.Any] = {
            "id": 1,
            "name": "Test1",
            "value": 10.1,
        }
        entity_deserialized2: TestJsonEntity = JsonSerializerHelper.deserialize(entity_deserialized2_dict, TestJsonEntity)
        print("eneity 1 deserializer 2:", entity_deserialized2)
        self.assertIsInstance(entity_deserialized2, TestJsonEntity)

    def test_entity2(self):
        entity2: TestJsonEntity2 = TestJsonEntity2(id=2, name="Test2", value=20.5)
        entity2_serialized = JsonSerializerHelper.serialize(entity2)
        print("entity 2 serializer:", entity2_serialized)
        self.assertIsInstance(entity2_serialized, str)

        entity2_deserialized: TestJsonEntity2 = JsonSerializerHelper.deserialize(entity2_serialized, TestJsonEntity2)
        print("entity 2 deserializer:", entity2_deserialized)
        self.assertIsInstance(entity2_deserialized, TestJsonEntity2)

        entity2_deserialized2_dict: t.Dict[str, t.Any] = {
            "id": 2,
            "name": "Test2-1",
            "value": 20.1,
        }
        entity2_deserialized2: TestJsonEntity2 = JsonSerializerHelper.deserialize(entity2_deserialized2_dict, TestJsonEntity2)
        print("entity 2 deserializer 2:", entity2_deserialized2)
        self.assertIsInstance(entity2_deserialized2, TestJsonEntity2)

    def test_entity3(self):
        entity3: TestJsonEntity3 = TestJsonEntity3.build(id=3, name="Test3", value=30.5)
        entity3_serialized = JsonSerializerHelper.serialize(entity3)
        print("entity 3 serializer:", entity3_serialized)
        self.assertIsInstance(entity3_serialized, str)

        entity3_deserialized: TestJsonEntity3 = JsonSerializerHelper.deserialize(entity3_serialized, TestJsonEntity3.build)
        print("entity 3 deserializer:", entity3_deserialized)
        self.assertIsInstance(entity3_deserialized, TestJsonEntity3)

        entity3_deserialized2_dict: t.Dict[str, t.Any] = {
            "id": 3,
            "name": "Test3-1",
            "value": 30.1,
        }
        entity3_deserialized2: TestJsonEntity3 = JsonSerializerHelper.deserialize(entity3_deserialized2_dict, TestJsonEntity3.build)
        print("entity 3 deserializer 2:", entity3_deserialized2)
        self.assertIsInstance(entity3_deserialized2, TestJsonEntity3)

    def test_plain_dict(self):
        plain_dict = {
            "key1": [{"id": "1", "name": "1", "value": "10.0"}, {"id": "2", "name": "2", "value": "20.0"}],
            "key2": [{"id": "3", "name": "3", "value": "30.0"}, {"id": "4", "name": "4", "value": "40.0"}],
        }

        plain_dict_serialized = JsonSerializerHelper.serialize(plain_dict)
        print("plain dict serializer:", plain_dict_serialized)
        print("plain dict serializer raw:", repr(plain_dict_serialized))
        self.assertIsInstance(plain_dict_serialized, str)

    def test_entity_dict(self):
        entity = TestJsonEntity(1, "Test", 0.5)
        entity_dict = TestJsonEntityDict(id=1, eneity=entity)

        entity_dict_serialized = JsonSerializerHelper.serialize(entity_dict)
        print("entity dict serializer:", entity_dict_serialized)
        self.assertIsInstance(entity_dict_serialized, str)

        # entity_dict_deserialized: TestJsonEntityDict = JsonSerializerHelper.deserialize(entity_dict_serialized, TestJsonEntityDict)
        # print("entity dict deserializer:", entity_dict_deserialized)
        # self.assertIsInstance(entity_dict_deserialized, TestJsonEntityDict)

    def test_schema(self):
        formdata = {
            "name": "Alice",
            "email": "alice@example.com",
            "userRule": "admin",
            "address_id": 123,
        }

        user_dto = UserDTO(**formdata)

        print(user_dto)
        # print(user_dto.to_dict())
        # print(user_dto.to_serializable_dict())
        # print(user_dto.to_json_string())
        # print(user_dto.hashcode)

        user = UserEntity.from_schema(user_dto)
        print(f"user entity 1: {user}")
        # 入库后返回ID
        user.id = 1001
        user.address = UserAddressEntity(id=1, address="1 Main St")
        print(type(user.address))
        user.address_id = user.address.id
        print(f"user entity 2: {user}")

        user_vo = UserVO.from_model(user)
        print(f"user vo: {JsonSerializerHelper.serialize(user_vo.to_dict())}")

        time.time()


if __name__ == "__main__":
    unittest.main()
