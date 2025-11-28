# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-05-19 14:15:55 UTC+08:00
"""

import os
from pathlib import Path

ROOT_PATH = Path(__file__).resolve().parent.parent

DEV_CONFIG_FILE_PATH = os.path.join(ROOT_PATH, "conf", "dev", "config.yaml")
