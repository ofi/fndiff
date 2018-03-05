"""
    FilenamesDiffer.py -- Main class of FilenamesDiff

    See LICENSE for copyright details.
"""

import re
from FilenamesSelection import FilenamesSelection

class FilenamesDiffError(Exception):

    def __init__(self, errString, args):
        self.__errstring = errString
        self.__args = args
    
    def __str__(self):
        return self.__errstring


class FilenamesDiffer:
    """Main class of operation."""
    
    def __init__(self, **kwargs):
        try:
            self.__src_selection = FilenamesSelection(
                kwargs['srcdir'], kwargs['pattern'], kwargs['reflag'])
            self.__dst_selection = FilenamesSelection(
                kwargs['dstdir'], kwargs['pattern'], kwargs['reflag'])
        except KeyError as err:
            raise FilenamesDiffError(
                "Argument to constructor is missing (was: {}).".format(err),
                kwargs)

    def diff(self):
        result = []
        try:
            src_dict = self.__src_selection.eval()
            dst_dict = self.__dst_selection.eval()
            result = [ dst_dict[x] for x in src_dict.keys()
                if not x in dst_dict]
        except Exception as err:
            raise FilenamesDiffError(
                "Invalid comparison: {}.".format(err),
                [self.__src_selection, self.__dst_selection])
        return result
