"""
    test_fndiff.py -- Tests

    See LICENSE for copyright details.
"""
from unittest import TestCase

import fndiff

import os
TESTDATA_PATH = os.path.join(os.path.dirname(__file__), 'data')


class TestFnDiff (TestCase):

    def setUp(self):
        self.jpg_dir = os.path.join(TESTDATA_PATH, 'JPG')
        self.raf_dir = os.path.join(TESTDATA_PATH, 'RAF')
        self.fuji_pattern = 'DSCF([0-9]+)[.].*$'

    def test_trivial(self):
        """Just ensure tests are found and running in general."""
        self.assertTrue(True)

    def test_diff_creation_fail(self):
        """Assert there's no FilenamesDiffer creation without arg's."""
        with self.assertRaises(fndiff.FilenamesDiffError):
            fndiff.FilenamesDiffer()

    def test_diff_usual(self):
        """Test usual case of missing JPGs in comparison to RAF."""
        raf_expected_result_set = { os.path.join(self.raf_dir, x)
            for x in [ 'DSCF01236.RAF', 'DSCF01234.RAF', 'DSCF01231.RAF',
                        'DSCF01233.RAF', 'DSCF01232.RAF']}
        result = fndiff.filenames_diff(self.raf_dir, self.jpg_dir,
            self.fuji_pattern, True)
        self.assertSetEqual(set(map(lambda x: str(x), result)),
            raf_expected_result_set)
        
    def test_diff_same_dir_error(self):
        """Assert failure on source directory == target directory."""
        with self.assertRaises(fndiff.FilenamesDiffError):
            fndiff.filenames_diff(self.jpg_dir, self.jpg_dir,
                self.fuji_pattern, True)