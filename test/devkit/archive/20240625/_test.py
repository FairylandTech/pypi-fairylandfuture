# coding: utf-8
""" 
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-06-25 14:07:46 UTC+08:00
"""

from dataclasses import dataclass, fields, make_dataclass, Field, field
from typing import Any, Dict, Type, TypeVar

# 定义一个泛型变量
T = TypeVar("T")

# 示例字典结构
example_dict = {"name": str, "age": int, "email": str, "is_active": bool}


# 动态生成 dataclass
def create_dataclass(class_name: str, field_dict: Dict[str, Type[Any]]) -> Type[Any]:
    # 生成字段列表，格式为 (name, type) 的元组
    fields_list = [(name, field_type) for name, field_type in field_dict.items()]
    # 使用 make_dataclass 动态生成 dataclass
    return make_dataclass(class_name, fields_list)


# 工厂类
class DataclassFactory:
    def __init__(self):
        self._classes: Dict[str, Type[Any]] = {}

    def register_class(self, class_name: str, field_dict: Dict[str, Type[Any]]):
        dataclass_type = create_dataclass(class_name, field_dict)
        self._classes[class_name] = dataclass_type

    def create_instance(self, class_name: str, **kwargs) -> T:
        if class_name not in self._classes:
            raise ValueError(f"Class {class_name} is not registered.")
        dataclass_type = self._classes[class_name]
        return dataclass_type(**kwargs)

    def get_registered_class(self, class_name: str) -> Type[T]:
        if class_name not in self._classes:
            raise ValueError(f"Class {class_name} is not registered.")
        return self._classes[class_name]


# 创建工厂实例
factory = DataclassFactory()

# 注册 dataclass
factory.register_class("Person", example_dict)

# 创建 dataclass 实例
person_instance = factory.create_instance("Person", name="John Doe", age=30, email="john.doe@example.com", is_active=True)

# 获取 dataclass 类型
PersonClass = factory.get_registered_class("Person")

# 由于我们知道 PersonClass 是一个 dataclass，我们可以这样使用它
another_person_instance = PersonClass(name="Jane Doe", age=25, email="jane.doe@example.com", is_active=False)

print(person_instance)
print(another_person_instance)
