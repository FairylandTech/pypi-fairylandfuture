# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-06-14 18:24:54 UTC+08:00
"""

import binascii

from fairylandfuture.enums.enconding import EncodingEnum
from fairylandfuture.modules.encryptions import UserPasswordEncryption
from fairylandfuture.modules.encryptions import Base64Encryption

if __name__ == "__main__":
    password = "123456"
    # password_salt = Cipher.generate_salt(128)
    # print(repr(password_salt))
    password_salt_str = """5?(1?,%$VfNZs/R$>837EOhH%(<_9rp$%B]M$/GlBcrW!3j~-k<r}Eupo!_k~|]Wxbi\'GUMb8vKWI:"Jj\\B\\p8(.(4dp[fCVjv/Q8RV,tY3:[I|XX8w|_WWNIay]s%d$"""
    encrypted_password, password_salt = UserPasswordEncryption.encrypt(password, password_salt_str)
    print(repr(encrypted_password))
    print(repr(binascii.unhexlify(password_salt).decode(EncodingEnum.utf8.value)))
    decrypted_password = UserPasswordEncryption.verify(password, encrypted_password, password_salt_str.encode(EncodingEnum.utf8.value).hex())
    print(repr(decrypted_password))
    #
    # key = "PxKl0fXCpI-colJRFR6m780U-pIGlAOTe6ni7C8eFZk=".encode(EncodingEnum.utf_8.value)
    # passwd = PasswordEncryption.encrypt("123456", key)
    # print(repr(passwd))
    # print(PasswordEncryption.decrypt("gAAAAABmbCPZNIb_2FZtUzBUuw16tCj5sySyFPNjsu7tL69OFx9vX8c3VdjCuWDRDmrBPg4-K1rzfxwTzptD-JMIoW_0SY0zbg==", key))
    string_1 = "Hello, World!"
    a = Base64Encryption.encode(string_1)
    print(repr(a))
    aa = "SGVsbG8sIFdvcmxkIQ=="
    print(repr(Base64Encryption.decode(aa)))
