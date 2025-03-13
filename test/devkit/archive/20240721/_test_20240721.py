# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-07-21 19:07:43 UTC+08:00
"""

from typing import MutableSequence, Sequence, List, Tuple, Mapping, MappingView, MutableMapping, KeysView

l = list()
t = tuple()
s = set()
d = dict()
d.update(a=1)

print(isinstance(l, MutableSequence))
print(isinstance(l, Sequence))

print(isinstance(t, MutableSequence))
print(isinstance(t, Sequence))
print(isinstance(s, MutableSequence))
print(isinstance(s, Sequence))
print("---")
print(isinstance(d, MutableSequence))
print(isinstance(d, Sequence))
print(isinstance(d, Mapping))
print(isinstance(d, MappingView))
print(isinstance(d, MutableMapping))
print(isinstance(d.keys(), KeysView))
