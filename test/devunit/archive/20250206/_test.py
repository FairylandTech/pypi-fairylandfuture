# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2025-02-06 04:52:06 UTC+08:00
"""
import hashlib
import os

from fairylandfuture.toolkits.encryption.cipher import UserPasswordCryptionToolkits, PasswordCryptionToolkits


def main():
    password = "Lionel0-12,./"
    salt = PasswordCryptionToolkits.generate_salt()
    print(salt)

    encrypted_password, salt_hex = UserPasswordCryptionToolkits.encrypt(password, salt)

    print(encrypted_password, bytes.fromhex(salt_hex).decode())


if __name__ == "__main__":
    main()
