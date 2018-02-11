"""
    FilenamesSelection.py -- Main class of FilenamesDiff

    See LICENSE for copyright details.
"""
from pathlib import Path

class FilenamesSelection:
    """Representation of a filename filter by pathname and pattern."""

    def check_path(self, dirStr):
        pass

    def __init__(self, dirStr, patternStr):
        self.__pathname = dirStr
        self.__pattern = patternStr

