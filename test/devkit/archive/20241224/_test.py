# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-12-24 18:04:26 UTC+08:00
"""

from fairylandfuture.toolkit.generic.structure import TreeBuilderV2

data = [
    {"id": 1, "parent_id": 0, "name": "China", "level": 1},
    {"id": 2, "parent_id": 1, "name": "Beijing", "level": 2},
    {"id": 3, "parent_id": 1, "name": "Shanghai", "level": 2},
    {"id": 4, "parent_id": 2, "name": "Dongcheng", "level": 3},
    {"id": 5, "parent_id": 2, "name": "Xicheng", "level": 3},
    {"id": 6, "parent_id": 3, "name": "Pudong", "level": 3},
    {"id": 7, "parent_id": 3, "name": "Huangpu", "level": 3},
    {"id": 8, "parent_id": 4, "name": "Dongzhimen", "level": 4},
    {"id": 9, "parent_id": 4, "name": "Dongsi", "level": 4},
    {"id": 10, "parent_id": 5, "name": "Xidan", "level": 4},
    {"id": 11, "parent_id": 5, "name": "Xisi", "level": 4},
    {"id": 12, "parent_id": 6, "name": "Lujiazui", "level": 4},
    {"id": 13, "parent_id": 6, "name": "Jinqiao", "level": 4},
    {"id": 14, "parent_id": 7, "name": "Nanjing Road", "level": 4},
    {"id": 15, "parent_id": 7, "name": "The Bund", "level": 4},
]

tree = TreeBuilderV2.build(data, max_depth=1)

import json

print(json.dumps(tree, indent=4))
