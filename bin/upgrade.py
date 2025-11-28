# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-08-24 14:01:31 UTC+08:00
"""

import os
import subprocess
import sys

from bin.generic import ROOT_PATH
from fairylandfuture.enums.encode import EncodingEnum


def main():
    print("Upgrade dependencies.")

    print("Step 1: Upgrade pip-tools.")
    upgrade_pip_tools = "pip install --no-cache-dir --upgrade pip-tools"
    _, upgrade_pip_tools_err = subprocess.Popen(upgrade_pip_tools.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()

    if upgrade_pip_tools_err:
        print("Upgrade pip-tools failed.")
        raise RuntimeError(upgrade_pip_tools_err.decode(EncodingEnum.UTF8.value))
    print("Upgrade pip-tools successfully.")

    print("Step 2: Generate requirements.")
    # generate_requirements = "pip-compile --upgrade --strip-extras --generate-hashes requirements.in"
    generate_requirements = "pip-compile --upgrade --strip-extras --generate-hashes --output-file=release-win-requirements.txt requirements.in"
    # The output information is in the error channel
    copy_requirements = "copy release-win-requirements.txt requirements.txt"
    subprocess.Popen(generate_requirements.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    subprocess.Popen(copy_requirements.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    print("Generate requirements successfully.")

    print("Step 3: Sync dependencies.")
    sync_requirements = "pip-sync requirements.txt"
    _, sync_requirements_err = subprocess.Popen(sync_requirements.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()

    if sync_requirements_err:
        print("Sync dependencies failed.")
        raise RuntimeError(sync_requirements_err.decode(EncodingEnum.UTF8.value))
    print("Sync dependencies successfully.")

    print("Step 4: Export develop dependencies.")
    if sys.platform == "win32":
        export_develop_dependencies = "pip freeze > dev-win-requirements.txt"
    else:
        export_develop_dependencies = "pip freeze > dev-linux-requirements.txt"

    _, export_develop_dependencies_err = subprocess.Popen(export_develop_dependencies.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()

    if export_develop_dependencies_err:
        print("Export develop dependencies failed.")
        raise RuntimeError(export_develop_dependencies_err.decode(EncodingEnum.UTF8.value))
    print("Export develop dependencies successfully.")

    print("Upgrade successfully.")


if __name__ == "__main__":
    sys.path.append(ROOT_PATH)
    os.chdir(ROOT_PATH)
    main()
