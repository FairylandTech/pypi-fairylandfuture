# coding: utf-8
""" 
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-06-30 15:10:23 UTC+08:00
"""

# from fairylandfuture.core.superclass.files import BaseFile, YamlFileMixin, JsonFileMixin

# file = BaseFile(r"C:\Lionel\Project\Github\pypi-fairylandfuture\fairylandfuture\modules\journal.py")
# file = BaseFile(r"C:\Users\Administrator\Downloads\immortalwrt-23.05.2-x86-64-generic-squashfs-combined.img")
# print(file.name, file.ext, file.size_byte, file.size_kilobyte, file.size_megabytes)
# file.max_size = 333 * (1024**2)
# print(file.md5, file.sha256)
# print(file.dir_path)

# json_file = JsonFileMixin(r"C:\Lionel\Project\Github\pypi-fairylandfuture\test\devkit\20240630\1.json")
# yaml_file = YamlFileMixin(r"C:\Lionel\Project\Github\pypi-fairylandfuture\test\devkit\20240630\2.yaml", True)
#
# data = json_file.load()
# print(data, type(data))
# yaml_file.save(data)
#
# yaml_file = YamlFileMixin(r"C:\Lionel\Project\Github\pypi-fairylandfuture\test\devkit\20240630\1.yaml")
# json_file = JsonFileMixin(r"C:\Lionel\Project\Github\pypi-fairylandfuture\test\devkit\20240630\2.json", True)
#
# data = yaml_file.load_yaml()
# print(data, type(data))
# json_file.save(data)

from fairylandfuture.modules.file.generic import File

file = File(r"C:\Lionel\Project\Github\pypi-fairylandfuture\test\devunit\20240630\2.json")
load_file = file.load_json()
print(repr(load_file))
save_file = File(r"C:\Lionel\Project\Github\pypi-fairylandfuture\test\devunit\20240630\3.yaml", True)
save_file.save_yaml(load_file)
