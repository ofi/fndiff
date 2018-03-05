"""
    FilenamesDiffer.py -- Main class of FilenamesDiff

    See LICENSE for copyright details.
"""

import re
from FilenamesSelection import FilenamesSelection

class FilenamesDiffError(Exception):

    def __init__(self, errString, args):
        self.__errstring = errString
        self.__args = str(args)
    
    def __str__(self):
        argstr = ""
        if self.__args:
            argstr = argstr.join(self.__args)
        return "{}, arguments: {}".format(self.__errstring, argstr)


class FilenamesDiffer:
    """Main class of operation."""
    
    def __init__(self, **kwargs):
        try:
            self.__src_selection = FilenamesSelection(
                kwargs['srcdir'], kwargs['pattern'], kwargs['reflag'])
            self.__dst_selection = FilenamesSelection(
                kwargs['dstdir'], kwargs['pattern'], kwargs['reflag'])
            if str(self.__src_selection) == str(self.__dst_selection):
                raise FilenamesDiffError(
                    "Sorry, this version can't operate in one single direcory"
                        + " with only one pattern.",
                    kwargs)
        except KeyError as err:
            raise FilenamesDiffError(
                "Argument to constructor is missing (was: {}).".format(err),
                kwargs)

    def not_in_target(self):
        """Return a list of Path objects, representing all files from source
            directory, which are not represented in the destination directory
            according to their pattern matches."""
        result = []
        try:
            src_dict = self.__src_selection.eval()
            dst_dict = self.__dst_selection.eval()
            result = [ src_dict[x] for x in src_dict.keys()
                if not x in dst_dict ]
        except Exception as err:
            raise FilenamesDiffError(
                "Invalid comparison: {}.".format(err),
                [self.__src_selection, self.__dst_selection])
        return result
