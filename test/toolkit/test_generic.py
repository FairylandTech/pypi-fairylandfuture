# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2025-11-27 15:00:00 UTC+08:00
"""

import unittest
from test import TestBase

from fairylandfuture.toolkit.utils.generic import GenericToolkit


class GenericToolkitTestCase(TestBase):
    """Test cases for GenericToolkit utility functions."""

    def test_format_filesize_zero(self):
        """Test formatting of zero bytes."""
        result = GenericToolkit.format_filesize(0)
        self.assertEqual(result, "0B")

    def test_format_filesize_bytes(self):
        """Test formatting of bytes (less than 1KB)."""
        result = GenericToolkit.format_filesize(500)
        self.assertEqual(result, "500.0 B")

    def test_format_filesize_kilobytes(self):
        """Test formatting of kilobytes."""
        result = GenericToolkit.format_filesize(1024)
        self.assertEqual(result, "1.0 KB")

        result = GenericToolkit.format_filesize(1536)
        self.assertEqual(result, "1.5 KB")

    def test_format_filesize_megabytes(self):
        """Test formatting of megabytes."""
        result = GenericToolkit.format_filesize(1048576)
        self.assertEqual(result, "1.0 MB")

        result = GenericToolkit.format_filesize(2621440)
        self.assertEqual(result, "2.5 MB")

    def test_format_filesize_gigabytes(self):
        """Test formatting of gigabytes."""
        result = GenericToolkit.format_filesize(1073741824)
        self.assertEqual(result, "1.0 GB")

    def test_format_filesize_terabytes(self):
        """Test formatting of terabytes."""
        result = GenericToolkit.format_filesize(1099511627776)
        self.assertEqual(result, "1.0 TB")


if __name__ == "__main__":
    unittest.main()
