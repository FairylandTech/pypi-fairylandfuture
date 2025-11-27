# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-06-04 10:38:31 UTC+08:00
"""

import json
import typing as t
from dataclasses import asdict, astuple, dataclass, field, fields

from fairylandfuture.models import BaseModel


@dataclass(frozen=False)
class BaseStructure:

    @property
    def asdict(self) -> dict[str, t.Any]:
        return asdict(self)

    @property
    def astuple(self) -> tuple[t.Any, ...]:
        return astuple(self)

    @property
    def string(self) -> str:
        return json.dumps(self.asdict, separators=(",", ":"), ensure_ascii=False)

    def to_dict(self, /, *, ignorenone: bool = False) -> dict[str, t.Any]:
        return {k: v for k, v in self.asdict.items() if v is not None} if ignorenone else self.asdict


@dataclass(frozen=True)
class BaseFrozenStructure:

    @property
    def asdict(self) -> dict[str, t.Any]:
        return asdict(self)

    @property
    def astuple(self) -> tuple[t.Any, ...]:
        return astuple(self)

    @property
    def string(self) -> str:
        return json.dumps(self.asdict, separators=(",", ":"), ensure_ascii=False)

    def to_dict(self, /, *, ignorenone: bool = False) -> dict[str, t.Any]:
        return {k: v for k, v in self.asdict.items() if v is not None} if ignorenone else self.asdict

    # @classmethod
    # def from_model(cls, model: BaseModel):
    #     kwargs: t.Dict[str, t.Any] = {}
    #     model_dict = model.to_dict()
    #     for field in fields(cls):
    #         if field.name in {f.name: f for f in fields(cls)}:
    #             kwargs.update({field.name: model_dict[field.name]})
    #
    #     return cls(**kwargs)

    @classmethod
    def from_model(cls, model: BaseModel):
        kwargs = {}
        model_dict = model.to_dict()
        for f in fields(cls):
            if f.name in model_dict:
                kwargs.update({f.name: model_dict.get(f.name)})

        return cls(**kwargs)


@dataclass
class BaseStructureTreeNode:
    id: t.Any
    parent_id: t.Any
    data: dict[str, t.Any]
    children: list["BaseStructureTreeNode"] = field(default=None)

    def __post_init__(self):
        self.children = []

    def get_id(self) -> t.Any:
        return self.id

    def get_parent_id(self) -> t.Any:
        return self.parent_id

    def add_child(self, child: "BaseStructureTreeNode"):
        self.children.append(child)

    def get_children(self) -> list["BaseStructureTreeNode"]:
        return self.children

    def to_dict(self) -> dict[str, t.Any]:
        result = {"id": self.id, "parent_id": self.parent_id, "data": self.data, "children": [child.to_dict() for child in self.children]}
        return result
