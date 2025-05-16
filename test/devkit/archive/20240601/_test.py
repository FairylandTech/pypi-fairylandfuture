# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-06-02 12:02:50 UTC+08:00
"""

from fairylandfuture.enums.chron import DateTimeEnum
from fairylandfuture.modules.datetimes import DateTimeModule
from fairylandfuture.toolkit.utils import journal
from fairylandfuture.toolkit.utils import LocalNetworkUtils

ts = DateTimeModule.datetime_to_timestamp("2024-06-03", _format=DateTimeEnum.DATE)

journal.debug("测试DEBUG日志")
journal.debug(str(ts))
journal.debug(LocalNetworkUtils.default_ip_address())
