# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2025-02-06 04:52:06 UTC+08:00
"""

from fairylandfuture.toolkit.utils.encryption.cipher import UserPasswordCryptionUtils, PasswordCryptionUtils


def main():
    password = "Lionel0-12,./"
    salt = PasswordCryptionUtils.generate_salt()
    print(salt)

    encrypted_password, salt_hex = UserPasswordCryptionUtils.encrypt(password, salt)

    print(encrypted_password, bytes.fromhex(salt_hex).decode())


if __name__ == "__main__":
    main()
