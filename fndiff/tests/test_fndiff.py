"""
    test_fndiff.py -- Tests

    See LICENSE for copyright details.
"""
from unittest import TestCase

# from fndiff import fndiff, FilenamesDiffer, FilenamesDiffError
import fndiff

class TestFnDiff (TestCase):

    def test_trivial(self):
        self.assertTrue(True)

    def test_diff_creation(self):
        with self.assertRaises(fndiff.FilenamesDiffError):
            fndiff.FilenamesDiffer()
