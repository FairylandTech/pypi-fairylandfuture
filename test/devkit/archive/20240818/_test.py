# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-08-18 00:40:48 UTC+08:00
"""

from fairylandfuture.toolkit.journal import Journal
from fairylandfuture.tools.files.general import YamlFile

journal = Journal(console=True)

journal.info("INFO ...")

file = YamlFile("test.yaml", create=True)

data = {"data": "test", "data2": [1, 2, 3, 4, 5], "data3": {"data": "test", "data1": "test1"}}

save_path = file.save_yaml(data)

journal.debug(f"save path: {save_path}")
