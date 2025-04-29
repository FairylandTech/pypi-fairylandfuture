# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2025-04-29 12:52:00 UTC+08:00
"""
from __future__ import nested_scopes, generators, division, absolute_import, with_statement, print_function, unicode_literals


from fairylandfuture.modules.journal import Journal

def run():
    journal = Journal(debug=True, serialize=True, console=True)

    journal.info("Runing ...")
