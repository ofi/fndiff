#!/usr/bin/env python3
"""
    fndiff-shfront.py -- List unpaired files in directories acc. to basenames

    See LICENSE for copyright details.
"""

import re
import FilenamesDiffer

def write_result(list, ofile):
    result = 0
    try:
        pass
    except Exception as err:
        pass
    else:
        pass
    finally:
        pass
    return result

def main(sdir, spat, tdir, tpat, rexflag, cpat, ofile):
    result = 0
    try:
        differ = FilenamesDiffer.FilenamesDiffer(srcdir=sdir, srcpattern=spat,
            dstdir=tdir, dstpat=tpat, reflag=rexflag)
        fnlist = differ.diff_it(cpat)
        result = write_result(fnlist, ofile)
    except FilenamesDiffer.FilenamesDiffError as err:
        result = err
    return result


if __name__ == '__main__':
    import argparse
    import sys

    parser = argparse.ArgumentParser(description='DiffBasenames')
    parser.add_argument('-S', '--source-dir', default='.',
        help='Source directory serving as reference (default: cwd)')
    parser.add_argument('-s', '--source-pattern', default='*',
        help='Pattern of files to consider in source directory (default: all)')
    parser.add_argument('-T', '--target-dir', required=True,
        help='Target directory with files to compare by common pattern to source')
    parser.add_argument('-t', '--target-pattern', default='*',
        help='Pattern of files to consider in target directory (default: all)')
    parser.add_argument('-r', '--regex', action='store_true',
        help='Set to indicate file patterns contain regular expressions '
            + '(instead of shell-style glob patterns, the default)')
    parser.add_argument('-c', '--common-pattern', default=r'(.*)[.].*$',
        help='Regular expression to match files from source and target sets '
            + 'containing a RE group to denominate the common part of each '
            + '(default is basename, i.e. all characters up to last dot)')
    parser.add_argument('outfile',
        help='Output file for result (default: stdout)')
    args = parser.parse_args()
    result = main(args.source_dir, args.source_pattern, args.target_dir,
        args.target_suffix, args.regex, re.escape(args.common_pattern),
        args.outfile)
    sys.exit(result)
