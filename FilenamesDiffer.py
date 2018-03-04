"""
    FilenamesDiffer.py -- Main class of FilenamesDiff

    See LICENSE for copyright details.
"""

from FilenamesSelection import FilenamesSelection

class FilenamesDiffError(Exception):

    def __init__(self, errString, args):
        self.__errstring = errString
    
    def __str__(self):
        return self.__errstring


class FilenamesDiffer:
    """Main class of operation."""
    
    def __init__(self, **kwargs):
        try:
            self.__srcSelection = FilenamesSelection(
                kwargs['srcdir'], kwargs['srcpattern'], kwargs['reflag'])
            self.__dstSelection = FilenamesSelection(
                kwargs['dstdir'], kwargs['dstpattern'], kwargs['reflag'])
        except KeyError as err:
            raise FilenamesDiffError(
                "Argument to constructor is missing (was: {}).".format(err),
                kwargs)

    def diff_it(self):
        pass



