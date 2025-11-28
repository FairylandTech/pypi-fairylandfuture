# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2025-11-28 17:26:00 UTC+08:00
"""

import unittest

from test import TestBase


class ImportsTestCase(TestBase):
    """Test clean import patterns for the fairylandfuture package."""

    def test_root_imports(self):
        """Test imports from the root package."""
        from fairylandfuture import Journal, SingletonJournal
        self.assertIsNotNone(Journal)
        self.assertIsNotNone(SingletonJournal)

    def test_abstract_imports(self):
        """Test imports from abstract module."""
        from fairylandfuture.abstract import AbstractMySQLOperator, AbstractPostgreSQLOperator
        self.assertIsNotNone(AbstractMySQLOperator)
        self.assertIsNotNone(AbstractPostgreSQLOperator)

    def test_core_imports(self):
        """Test imports from core module."""
        from fairylandfuture.core import SingletonMeta, BaseEnum, BaseStructure
        self.assertIsNotNone(SingletonMeta)
        self.assertIsNotNone(BaseEnum)
        self.assertIsNotNone(BaseStructure)

    def test_core_metaclass_imports(self):
        """Test imports from core.metaclass module."""
        from fairylandfuture.core.metaclass import SingletonMeta
        self.assertIsNotNone(SingletonMeta)

    def test_core_superclass_imports(self):
        """Test imports from core.superclass module."""
        from fairylandfuture.core.superclass import BaseEnum, BaseProgramException, BaseStructure
        self.assertIsNotNone(BaseEnum)
        self.assertIsNotNone(BaseProgramException)
        self.assertIsNotNone(BaseStructure)

    def test_builder_imports(self):
        """Test imports from builder module."""
        from fairylandfuture.builder import TreeBuilderToolkit, TreeBuilderToolkitV2
        self.assertIsNotNone(TreeBuilderToolkit)
        self.assertIsNotNone(TreeBuilderToolkitV2)

    def test_common_imports(self):
        """Test imports from common module."""
        from fairylandfuture.common import File, TextFile, ParamsValidator
        self.assertIsNotNone(File)
        self.assertIsNotNone(TextFile)
        self.assertIsNotNone(ParamsValidator)

    def test_enums_imports(self):
        """Test imports from enums module."""
        from fairylandfuture.enums import DateTimeEnum, EncodingEnum, FileModeEnum, LogLevelEnum
        self.assertIsNotNone(DateTimeEnum)
        self.assertIsNotNone(EncodingEnum)
        self.assertIsNotNone(FileModeEnum)
        self.assertIsNotNone(LogLevelEnum)

    def test_enums_datetime_imports(self):
        """Test imports from enums.datetime module."""
        from fairylandfuture.enums.datetime import DateTimeEnum, TimeZoneEnum
        self.assertIsNotNone(DateTimeEnum)
        self.assertIsNotNone(TimeZoneEnum)

    def test_exceptions_imports(self):
        """Test imports from exceptions module."""
        from fairylandfuture.exceptions import SQLExecutionException, ValidationError
        self.assertIsNotNone(SQLExecutionException)
        self.assertIsNotNone(ValidationError)

    def test_helpers_imports(self):
        """Test imports from helpers module."""
        from fairylandfuture.helpers import JsonEncoder, JsonSerializerHelper
        self.assertIsNotNone(JsonEncoder)
        self.assertIsNotNone(JsonSerializerHelper)

    def test_helpers_json_imports(self):
        """Test imports from helpers.json module."""
        from fairylandfuture.helpers.json import JsonEncoder, JsonSerializerHelper
        self.assertIsNotNone(JsonEncoder)
        self.assertIsNotNone(JsonSerializerHelper)

    def test_models_imports(self):
        """Test imports from models module."""
        from fairylandfuture.models import BaseModel
        self.assertIsNotNone(BaseModel)

    def test_structures_imports(self):
        """Test imports from structures module."""
        from fairylandfuture.structures import MySQLExecuteFrozenStructure, ResponseStructure
        self.assertIsNotNone(MySQLExecuteFrozenStructure)
        self.assertIsNotNone(ResponseStructure)

    def test_structures_database_imports(self):
        """Test imports from structures.database module."""
        from fairylandfuture.structures.database import MySQLExecuteFrozenStructure, PostgreSQLExecuteFrozenStructure
        self.assertIsNotNone(MySQLExecuteFrozenStructure)
        self.assertIsNotNone(PostgreSQLExecuteFrozenStructure)

    def test_utils_imports(self):
        """Test imports from utils module."""
        from fairylandfuture.utils import DateTimeUtils
        self.assertIsNotNone(DateTimeUtils)

    def test_utils_validator_imports(self):
        """Test imports from utils.validator module."""
        from fairylandfuture.utils.validator import StringValidatorUtils
        self.assertIsNotNone(StringValidatorUtils)


if __name__ == "__main__":
    unittest.main()
