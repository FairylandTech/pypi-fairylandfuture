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


def counter(token):
    url = "https://api.github.com/repos/FairylandTech/pypi-fairylandfuture/commits"
    headers = {"Authorization": f"Bearer {token}"}
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


def process(data=None):
    if not data:
        with open("fairylandfuture/conf/release/buildversion", "r", encoding="UTF-8") as file:
            content = file.read()

        data = str(int(content.strip()) + 1)

    with open("fairylandfuture/conf/release/buildversion", "w", encoding="UTF-8") as file:
        file.write(data)


if __name__ == "__main__":
    TOKEN = os.environ.get("GITHUB_TOKEN")
    count = counter(TOKEN)
    if count:
        process(str(count + 2))
        print("Build version updated successfully.")
    else:
        print("Failed to retrieve commit count.")
        process()
        exit(1)
