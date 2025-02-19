# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2025-01-07 17:42:31 UTC+08:00
"""

from dataclasses import dataclass
from typing import Dict

from fairylandfuture.core.superclass.structures import BaseStructureTreeNode
from fairylandfuture.toolkits.generic.structure import TreeBuilder, TreeBuilderV2


@dataclass
class TreeNode(BaseStructureTreeNode):

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "parent_id": self.parent_id,
            "code": self.data.get("code"),
            "children": [child.to_dict() for child in self.children],
        }


class TreeBuilderV3(TreeBuilder):
    node = TreeNode


if __name__ == "__main__":
    data = [
        {"id": 1, "parent_id": 0, "code": "root"},
        {"id": 2, "parent_id": 1, "code": "child1"},
        {"id": 3, "parent_id": 1, "code": "child2"},
        {"id": 4, "parent_id": 2, "code": "child1.1"},
        {"id": 5, "parent_id": 2, "code": "child1.2"},
        {"id": 6, "parent_id": 3, "code": "child2.1"},
        {"id": 7, "parent_id": 3, "code": "child2.2"},
    ]

    tree = TreeBuilderV3.build(data)
    print(tree)
