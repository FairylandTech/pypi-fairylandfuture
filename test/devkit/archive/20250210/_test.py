# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2025-02-10 20:42:59 UTC+08:00
"""


def example_function():
    try:
        return "Returning from try"
    except Exception:
        return "Returning from except"
    finally:
        print("This will always execute")


if __name__ == "__main__":
    result = example_function()
    print(result)
