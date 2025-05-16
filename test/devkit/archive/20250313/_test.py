# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2025-03-13 23:06:09 UTC+08:00
"""
from fairylandfuture.structures.http.response import ResponseStructure


def main():
    response = ResponseStructure()

    response.code = 200
    response.data = {}

    print(response.asdict)


if __name__ == "__main__":
    main()
