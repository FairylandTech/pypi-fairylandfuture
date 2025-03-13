# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-06-02 12:02:50 UTC+08:00
"""

from fairylandfuture.enums.chrono import DateTimeEnum
from fairylandfuture.modules.datetimes import DateTimeModule
from fairylandfuture.utils.journal import journal
from fairylandfuture.utils.networking.local import LocalNetworkUtils

ts = DateTimeModule.datetime_to_timestamp("2024-06-03", _format=DateTimeEnum.date)

journal.debug("测试DEBUG日志")
journal.debug(str(ts))
journal.debug(LocalNetworkUtils.default_ip_address())
