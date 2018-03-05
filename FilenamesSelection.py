"""
    FilenamesSelection.py -- Main class of FilenamesDiff

    See LICENSE for copyright details.
"""
from pathlib import Path
import fnmatch
import re
import os

class FilenamesSelectionError(Exception):

    def __init__(self, dirStr, patStr, mStr):
        super().__init__()
        self.__dir = dirStr
        self.__pat = patStr
        self.__msg = mStr
    
    def __str__(self):
        return "{}. Directory: {}, pattern {})".format(
            self.__msg, self.__dir, self.__pat)



class FilenamesSelection:
    """Representation of a filename filter by pathname (no wildcards) and
        pattern (may contain wildcards).
    """

    def eval(self):
        """Return a dictionary with tuple of matching groups from pattern or
            the whole match as key and the full path as values according to
            receiver's directory path and file name pattern."""
        result = {}
        mx = lambda x: self.__regex.match(x)
        try:
            if self.__regex.groups > 0:
                tx = lambda x: mx(x).groups()
            else:
                tx = lambda x: (mx(x).string, ) 
            result = dict((tx(f), self.__path / f)
                    for f in os.listdir(self.__path)
                    if mx(f) and Path(self.__path / f).is_file())
        except Exception as err:
            raise FilenamesSelectionError(self.__path, self.__regex.pattern,
                "Error evaluating regular expression: {}".format(err))
        return result
    
    
    def __str__(self):
        return "FilenamesSelection of ({}, {})".format(
            self.__path, self.__regex)


    def __init__(self, dirStr, patternStr, reflag=False):
        """Construct a FilenameSelection from the given dirStr, which should
            contain a relative or absolute local filesystem path, and a filename
            pattern to filter for files. If the optional reflag is set, the
            pattern will be interpreted as a regular expresion, otherwise it
            will be translated from assumed shell glob pattern."""
        try:
            self.__path = Path(dirStr).expanduser()
        except TypeError as err:
            raise FilenamesSelectionError(dirStr, patternStr,
                "Invalid path string given (was: {})".format(err))
        else:
            if not self.__path.exists():
                raise FilenamesSelectionError(dirStr, patternStr,
                    "Path {} does not exist".format(self.__path))
        try:
            if reflag:
                self.__regex = re.compile(patternStr)
            else:
                self.__regex = re.compile(fnmatch.translate(patternStr))
        except Exception as ex:
            raise FilenamesSelectionError(dirStr, patternStr,
                "Invalid regular expression for pattern (was: {})".format(ex))
        


if __name__ == '__main__':
    td = FilenamesSelection('.', '*.py')
    print("{} evaluates to: {}".format(td, td.eval()))
    te = FilenamesSelection('/var/log/', r'(.*)[.]([0-9]+)*[.]bz[0-9]?$', True)
    print("{} evaluates to: {}".format(te, te.eval()))
    tf = FilenamesSelection('~/Music', 'iTunes', False)
    print("{} evaluates to: {}".format(tf, tf.eval()))
