# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2025-05-26 13:12:15 UTC+08:00
"""

import tomllib

def main():
    # This is a placeholder for the main function.
    # You can add your code here to execute when the script runs.
    print("Hello, World!")

    read_toml()

def read_toml():
    with open("pyproject.toml", "rb") as f:
        data = tomllib.load(f)

    print(data)

    print(data.get("project", {}).get("version", "0.0.0"))


if __name__ == '__main__':
    main()


