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
                kwargs['srcdir'], kwargs['srcpat'], kwargs['reflag'])
            self.__dst_selection = FilenamesSelection(
                kwargs['dstdir'], kwargs['dstpat'], kwargs['reflag'])
        except KeyError as err:
            raise FilenamesDiffError(
                "Argument to constructor is missing (was: {}).".format(err),
                kwargs)

    def diff_it(self, common_pattern):
        result = []
        try:
            rx = re.compile(common_pattern)
            # build group set from source
            # build group set from target
            # extract set of files in target not present in source
            # convert to sorted list
        except Exception as err:
            raise FilenamesDiffError(
                "Invalid comparison: {}, using pattern {}.".format(err,
                common_pattern), common_pattern)
        return result
