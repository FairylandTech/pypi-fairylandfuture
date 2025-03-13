# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-08-21 21:33:29 UTC+08:00
"""

from typing import Dict, Any

from fairylandfuture.tools.files.general import YamlFile, JsonFile

json_file = YamlFile("test.yaml")
data: Dict[str, Any] = json_file.load_yaml()
print(data.get("a"))
