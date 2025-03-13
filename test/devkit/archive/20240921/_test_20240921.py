# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-09-21 17:54:34 UTC+08:00
"""

import pkgutil
import inspect
import importlib


def list_subpackages(package):
    subpackages = [name for _, name, ispkg in pkgutil.walk_packages(package.__path__)]
    return subpackages


def list_modules(package):
    modules = [name for _, name, ispkg in pkgutil.walk_packages(package.__path__) if not ispkg]
    return modules


def list_classes(package):
    classes = [member for member in dir(package) if inspect.isclass(getattr(package, member))]
    return classes


def main(package_name):
    package = importlib.import_module(package_name)

    # 获取子包
    subpackages = list_subpackages(package)
    print(f"Subpackages ({len(subpackages)}): {subpackages}")

    # 获取模块
    modules = list_modules(package)
    print(f"Modules ({len(modules)}): {modules}")

    # 获取类
    classes = list_classes(package)
    print(f"Classes ({len(classes)}): {classes}")


# 使用示例
main("fairylandfuture")
