# @software: PyCharm
# @author: Lionel Johnson
# @contact: https://fairy.host
# @organization: https://github.com/FairylandFuture
# @datatime: 2024-05-09 16:38:27 UTC+08:00

# This script is used to build and upload a Python package to PyPI.
# It assumes that the package has already been built and is located in the dist directory.
# It also assumes that the dev-requirements.txt file is located in the same directory as the script.
# It also assumes that the Tsinghua University PyPI mirror is used.

# To use this script, you need to have Python installed on your system and have pip installed.
# You also need to have the twine package installed, which you can install by running the following command:
# pip install twine

# To run the script, simply execute the following command in PowerShell:

Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force

$ProjectPyPIrcPath = "conf\pypi\.pypirc"
$PyPIrcPath = "$HOME\.pypirc"

if (-Not (Test-Path $PyPIrcPath))
{
    if (-Not (Test-Path $ProjectPyPIrcPath))
    {
        Write-Host "The file .pypirc does not exist"
        exit
    }
    else
    {
        Copy-Item -Path $ProjectPyPIrcPath -Destination $PyPIrcPath -Force
    }
}
else
{
    Write-Host "The file .pypirc already exists in the home directory. No action taken."
}

# Install the required packages and build the package
pip install --no-cache-dir -r dev-win-requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
python -m build --no-isolation
# If you want to upload to the official PyPI repository, use the following command instead:
twine upload dist/*
# If you want to upload to the test PyPI repository, use the following command instead:
#twine upload --repository testpypi dist/*
Remove-Item -Path .\dist, .\*.egg-info -Recurse -Force
