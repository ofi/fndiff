"""
    fnselection.py -- Representation of a pattern based selection of files.

    See LICENSE for copyright details.
"""
from pathlib import Path
import fnmatch
import re
import os

class FilenamesSelectionError(Exception):

    def __init__(self, dir_str, pat_str, msg):
        super().__init__()
        self.__dir = dir_str 
        self.__pat = pat_str
        self.__msg = msg
    
    def __str__(self):
        return "{}. Directory: {}, pattern {})".format(
            self.__msg, self.__dir, self.__pat)



class FilenamesSelection:
    """Representation of a filename filter by pathname (no wildcards) and
        pattern (may contain wildcards and regular expression groups).
    """

    def __init__(self, dir_str, pattern_str, reflag=False):
        """Construct a FilenameSelection from the given  dir_str, which should
            contain a relative or absolute local filesystem path, and a filename
            pattern to filter for files. If the optional reflag is set, the
            pattern will be interpreted as a regular expresion, otherwise it
            will be translated from assumed shell glob pattern."""
        try:
            self.__path = Path(dir_str).expanduser()
        except TypeError as err:
            raise FilenamesSelectionError(dir_str, pattern_str,
                "Invalid path string given (was: {})".format(err))
        else:
            if not self.__path.exists():
                raise FilenamesSelectionError(dir_str, pattern_str,
                    "Path {} does not exist".format(self.__path))
        try:
            if reflag:
                self.__regex = re.compile(pattern_str)
            else:
                self.__regex = re.compile(fnmatch.translate(pattern_str))
        except Exception as ex:
            raise FilenamesSelectionError( dir_str, pattern_str,
                "Invalid regular expression for pattern (was: {})".format(ex))
        
    def __str__(self):
        return "FilenamesSelection of ({}, {})".format(
            self.__path, self.__regex)

    def eval(self):
        """Return a dictionary with tuple of matching groups from pattern or
            the whole match as keys and the full path as values according to
            receiver's directory path and file name pattern."""
        result = {}
        mx = lambda x: self.__regex.match(x)
        try:
            if self.__regex.groups > 0:
                tx = lambda x: mx(x).groups()
            else:
                tx = lambda x: (mx(x).string, ) 
            flist = os.listdir(self.__path)
            result = dict((tx(f), self.__path / f)
                    for f in flist
                    if mx(f) and (self.__path / f).is_file())
        except Exception as err:
            raise FilenamesSelectionError(self.__path, self.__regex.pattern,
                "Error evaluating regular expression: {}".format(err))
        return result
    
 

if __name__ == '__main__':
    td = FilenamesSelection('.', '*.py')
    print("{} evaluates to: {}".format(td, td.eval()))
    # te = FilenamesSelection('/var/log/', r'(.*)[.]([0-9]+)*[.]bz[0-9]?$', True)
    # print("{} evaluates to: {}".format(te, te.eval()))
    # tf = FilenamesSelection('~/Music', 'iTunes', False)
    # print("{} evaluates to: {}".format(tf, tf.eval()))
    tt = FilenamesSelection('test/src', 'DSCF([0-9]{5})[.][A-Z]{3}$',  True)
    print("{} evaluates to: {}".format(tt, tt.eval()))
