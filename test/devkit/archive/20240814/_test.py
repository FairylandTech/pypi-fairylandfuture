# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-08-14 17:13:15 UTC+08:00
"""

from fairylandfuture.structures.http.response import ResponseFrozenStructure


if __name__ == "__main__":
    data = {"key": '["asdsa"]'}
    response = ResponseFrozenStructure(code=200, data=data)
    d = response.asdict
    d.update(code=2000)
    print(repr(response), repr(response.to_dict(ignorenone=True)), repr(d))
