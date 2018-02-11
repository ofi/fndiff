"""
    FilenamesDiffer.py -- Main class of FilenamesDiff

    See LICENSE for copyright details.
"""

class FilenamesDiffError(Exception):

    def __init__(self, errString, args):
        self.__errstring = errString
    
    def __str__(self):
        return self.__errstring


class FilenamesDiffer:
    """Main class of operation."""
    
    def __init__(self, **kwargs):
        pass

    def diff_it(self):
        pass



