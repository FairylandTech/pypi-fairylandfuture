# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-06-26 00:09:01 UTC+08:00
"""

import os
import sys
import platform

from fairylandfuture.const.enums import PlatformEnum

from fairylandfuture.utils.general.common import OSPlatform

print(PlatformEnum.windows.value)

print(sys.platform)
print(platform.architecture())
print(platform.system())
print(platform.node())

print(OSPlatform.get_os_platform())
print(sys.version)
print(sys.version_info.major, sys.version_info.minor)
print(sys.version.split()[0])

# print(os.getgid())
# print(os.getgid())
