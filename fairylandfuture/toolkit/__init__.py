# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-08-10 18:23:28 UTC+08:00
"""

# Journal
from fairylandfuture.toolkit.journal import Journal, SingletonJournal

# Tools
from fairylandfuture.toolkit.tools import (
    File,
    TextFile,
    YamlFile,
    JsonFile,
    OtherTextFile,
    HTTPSimpleRequest,
    ParamsValidator,
)

# Utils
from fairylandfuture.toolkit.utils import (
    # Builder
    TreeBuilderToolkit,
    TreeBuilderToolkitV2,
    # Chron
    DateTimeToolkit,
    # Decorators
    TryCatchMethodDecorator,
    # Encryption
    CipherToolkit,
    UserPasswordCryptionToolkit,
    PasswordCryptionToolkit,
    Base64CryptionToolkit,
    # Faker
    FakeGeneralToolkit,
    FakeNetworkToolkit,
    FakeUserToolkit,
    # General
    OSPlatform,
    DefaultConstantToolkit,
    APIConstantToolkit,
    EncodingConstantToolkit,
    # Network
    LocalNetworkToolkit,
    # Parser
    UserAgentParserToolkit,
    # Request
    DjangoRequestToolkit,
    # Validation
    StringValidatorToolkit,
)

__all__ = [
    # Journal
    "Journal",
    "SingletonJournal",
    # Tools - File
    "File",
    "TextFile",
    "YamlFile",
    "JsonFile",
    "OtherTextFile",
    # Tools - HTTP
    "HTTPSimpleRequest",
    # Tools - Validator
    "ParamsValidator",
    # Utils - Builder
    "TreeBuilderToolkit",
    "TreeBuilderToolkitV2",
    # Utils - Chron
    "DateTimeToolkit",
    # Utils - Decorators
    "TryCatchMethodDecorator",
    # Utils - Encryption
    "CipherToolkit",
    "UserPasswordCryptionToolkit",
    "PasswordCryptionToolkit",
    "Base64CryptionToolkit",
    # Utils - Faker
    "FakeGeneralToolkit",
    "FakeNetworkToolkit",
    "FakeUserToolkit",
    # Utils - General
    "OSPlatform",
    "DefaultConstantToolkit",
    "APIConstantToolkit",
    "EncodingConstantToolkit",
    # Utils - Network
    "LocalNetworkToolkit",
    # Utils - Parser
    "UserAgentParserToolkit",
    # Utils - Request
    "DjangoRequestToolkit",
    # Utils - Validation
    "StringValidatorToolkit",
]
