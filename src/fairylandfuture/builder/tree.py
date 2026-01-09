# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-12-23 16:35:23 UTC+08:00
"""

import typing as t

from fairylandfuture.core.superclass.structure import BaseStructureTreeNode


class TreeBuilder:
    node = BaseStructureTreeNode

    @classmethod
    def build(cls, data: t.Sequence[dict[str, t.Any]], id_field: str = "id", parent_id_field: str = "parent_id") -> tuple[dict[str, t.Any], ...]:
        if not data:
            raise ValueError("Input data cannot be empty.")

        nodes: dict[str | int, BaseStructureTreeNode] = {
            item.get(id_field): cls.node(item.get(id_field), parent_id=item.get(parent_id_field), data=item) for item in data
        }
        root_nodes = []

        for node in nodes.values():
            parent_id = node.parent_id
            if parent_id and parent_id in nodes:
                nodes[parent_id].add_child(node)
            else:
                root_nodes.append(node)

        return tuple([node.to_dict() for node in root_nodes])


class TreeBuilderV2(TreeBuilder):
    @classmethod
    def build(
        cls,
        data: t.Sequence[dict[str, t.Any]],
        id_field: str = "id",
        parent_id_field: str = "parent_id",
        max_depth: int | None = None,
    ) -> tuple[dict[str, t.Any], ...]:
        if not data:
            raise ValueError("Input data cannot be empty.")

        nodes = {item.get(id_field): cls.node(item.get(id_field), parent_id=item.get(parent_id_field), data=item) for item in data}
        root_nodes = []

        for node in nodes.values():
            parent_id = node.parent_id
            if parent_id and parent_id in nodes:
                nodes[parent_id].add_child(node)
            else:
                root_nodes.append(node)

        return tuple([cls.__limit_depth(node.to_dict(), max_depth) for node in root_nodes])

    @classmethod
    def __limit_depth(cls, node: dict[str, t.Any], max_depth: int, current_depth: int = 1) -> dict[str, t.Any]:
        if max_depth is not None and current_depth >= max_depth:
            node.pop("children", None)
        else:
            children = node.get("children", [])
            node["children"] = [cls.__limit_depth(child, max_depth, current_depth + 1) for child in children]
        return node
