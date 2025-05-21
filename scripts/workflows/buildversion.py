# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-05-11 17:02:12 UTC+08:00
"""

import os

import requests


def count_commits(token):
    url = "https://api.github.com/repos/PrettiestFairy/pypi-fairylandfuture/commits"
    # headers = {"Authorization": f"Token {token}"}
    headers = {"Authorization": f"Bearer {token}"}
    # response = requests.get(url, headers=headers)
    # try:
    #     if response.status_code == 200:
    #         commit_data = response.json()
    #         print(f"Fetched {len(commit_data)} commits")
    #         return len(commit_data)
    #     else:
    #         print(f"Failed to fetch commits, status code: {response.status_code}")
    #         return 0
    # except Exception as err:
    #     print(f"Failed to fetch commits, error: {err}")
    #     return 0
    page = 1
    per_page = 100
    count = 0

    while True:
        response = requests.get(f"{url}?page={page}&per_page={per_page}", headers=headers)
        if response.status_code != 200:
            print(f"Request failed. HTTP status code：{response.status_code}")
            break

        current_batch = len(response.json())
        count += current_batch

        if current_batch < per_page:
            break

        page += 1

    return count


def write_commit_count(count):
    with open("fairylandfuture/conf/release/buildversion", "w", encoding="UTF-8") as file:
        file.write(count)
    with open("conf/release/buildversion", "w", encoding="UTF-8") as file:
        file.write(count)
    return "Successful"


if __name__ == "__main__":
    TOKEN = os.environ.get("GITHUB_TOKEN")
    commit_count = count_commits(TOKEN)
    if commit_count:
        commit_count += 2
        write_commit_count(str(commit_count))
