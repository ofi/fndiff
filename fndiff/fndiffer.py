"""
    fndiff.py -- Main class and function

    See LICENSE for copyright details.
"""

import re

from .fnselection import FilenamesSelection, FilenamesSelectionError

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
            srcdir = kwargs['srcdir']
            dstdir = kwargs['dstdir']
            pattern = kwargs['pattern']
            reflag = kwargs['reflag']
        except KeyError as err:
            raise FilenamesDiffError(
                "Argument to constructor is missing (was: {}).".format(err),
                kwargs)
        try:
            self.__src_selection = FilenamesSelection(srcdir, pattern, reflag)
            self.__dst_selection = FilenamesSelection(dstdir, pattern, reflag)
        except FilenamesSelectionError as err:
            raise FilenamesDiffError(
                "Error creating file selection (was: {}).".format(err),
                kwargs)
        if str(self.__src_selection) == str(self.__dst_selection):
            raise FilenamesDiffError(
                "Sorry, this version can't operate in one single direcory"
                    + " with only one pattern.",
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


def filenames_diff(sdir, tdir, pat, rexflag):
    """ Top level function to produce list of resulting file pathes as strings.
    """
    result = []
    differ = FilenamesDiffer(srcdir=sdir,
        dstdir=tdir, pattern=pat, reflag=rexflag)
    result = differ.not_in_target()
    return result
