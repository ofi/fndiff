"""
    fndiff.py - Main entry point of FilenamesDiffer
"""
import re
# from . import fndiffer
from .fndiffer import FilenamesDiffer, FilenamesDiffError

def fndiff(sdir, tdir, pat, rexflag, ofile):
    result = (0, "OK")
    try:
        differ = FilenamesDiffer(srcdir=sdir,
            dstdir=tdir, pattern=pat, reflag=rexflag)
        fnlist = differ.not_in_target()
        if ofile is None:
            for item in fnlist:
                print(item)
        else:
            with open(ofile, 'w') as f:
                f.writelines([ str(item) + '\n' for item in fnlist ]) 
    except FilenamesDiffError as err:
        result = (1, str(err))
    return result
