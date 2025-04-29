# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2025-04-23 09:49:49 UTC+08:00
"""

def main():

    suffix= "api/alert/downloadFile?path=order/file/20250423094949/漏洞.docx"

    print(suffix.split("path=")[1])


if __name__ == '__main__':
    main()