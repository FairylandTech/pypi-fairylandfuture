# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-08-08 23:00:45 UTC+08:00
"""

from collections import deque
from queue import Queue
from typing import Sequence

l = []
t = ()
s = set()

deq = deque()
que = Queue()

print(isinstance(deq, Sequence))
print(isinstance(que, Sequence))
