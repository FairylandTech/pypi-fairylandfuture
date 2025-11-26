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
from dataclasses import dataclass, asdict, astuple, field


@dataclass(frozen=False)
class BaseStructure:

    @property
    def asdict(self) -> t.Dict[str, t.Any]:
        return asdict(self)

    @property
    def astuple(self) -> t.Tuple[t.Any, ...]:
        return astuple(self)

    @property
    def string(self) -> str:
        return json.dumps(self.asdict, separators=(",", ":"), ensure_ascii=False)

    def to_dict(self, /, *, ignorenone: bool = False) -> t.Dict[str, t.Any]:
        return {k: v for k, v in self.asdict.items() if v is not None} if ignorenone else self.asdict

    def to_json(self, /, *, ignorenone: bool = False) -> t.Dict[str, t.Any]:
        return {k: v for k, v in self.asdict.items() if v is not None} if ignorenone else self.asdict

    def to_jsonstring(self: t.Self, /, *, ignorenone: bool = False) -> str:
        return json.dumps(self.to_json(ignorenone=ignorenone), separators=(",", ":"), ensure_ascii=False)


@dataclass(frozen=True)
class BaseFrozenStructure:

    @property
    def asdict(self) -> t.Dict[str, t.Any]:
        return asdict(self)

    @property
    def astuple(self) -> t.Tuple[t.Any, ...]:
        return astuple(self)

    @property
    def string(self) -> str:
        return json.dumps(self.asdict, separators=(",", ":"), ensure_ascii=False)

    def to_dict(self, /, *, ignorenone: bool = False) -> t.Dict[str, t.Any]:
        return {k: v for k, v in self.asdict.items() if v is not None} if ignorenone else self.asdict

    def to_json(self, /, *, ignorenone: bool = False) -> t.Dict[str, t.Any]:
        return {k: v for k, v in self.asdict.items() if v is not None} if ignorenone else self.asdict

    def to_jsonstring(self, /, *, ignorenone: bool = False) -> str:
        return json.dumps(self.to_json(ignorenone=ignorenone), separators=(",", ":"), ensure_ascii=False)


@dataclass
class BaseStructureTreeNode:
    id: t.Any
    parent_id: t.Any
    data: t.Dict[str, t.Any]
    children: t.List["BaseStructureTreeNode"] = field(default=None)

    def __post_init__(self):
        self.children = []

    def get_id(self) -> t.Any:
        return self.id

    def get_parent_id(self) -> t.Any:
        return self.parent_id

    def add_child(self, child: "BaseStructureTreeNode"):
        self.children.append(child)

    def get_children(self) -> t.List["BaseStructureTreeNode"]:
        return self.children

    def to_dict(self) -> t.Dict[str, t.Any]:
        result = {"id": self.id, "parent_id": self.parent_id, "data": self.data, "children": [child.to_dict() for child in self.children]}
        return result
