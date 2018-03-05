#!/usr/bin/env python3
"""
    fndiff-shfront.py -- List unpaired files in directories acc. to basenames

    See LICENSE for copyright details.
"""

import sys
import re
import FilenamesDiffer

def write_result(list, ofile):
    with open(ofile, 'w') as f:
        f.writelines(list)

def main(sdir, tdir, pat, rexflag, ofile):
    result = 0
    try:
        differ = FilenamesDiffer.FilenamesDiffer(srcdir=sdir,
            dstdir=tdir, pattern=pat, reflag=rexflag)
        fnlist = differ.diff()
        if ofile is None:
            for item in fnlist:
                print(item)
        else:
            with open(ofile, 'w') as f:
                f.writelines(fnlist) 
    except FilenamesDiffer.FilenamesDiffError as err:
        result = err
    return result


if __name__ == '__main__':
    import argparse
    import sys

    parser = argparse.ArgumentParser(description='DiffBasenames')
    parser.add_argument('-s', '--source-dir', default='.',
        help='Source directory serving as reference (default: cwd)')
    parser.add_argument('-t', '--target-dir', required=True,
        help='Target directory with files to compare by common pattern to source')
    parser.add_argument('-p', '--pattern', default=r'(.*)[.].*$',
        help='Regular expression to match files from source and target sets '
            + 'optionally containing one or more RE groups to denominate the'
            + 'common part(s) of each matching pair'
            + '(default is basename, i.e. all characters up to last dot)')
    parser.add_argument('-r', '--regex', action='store_true',
        help='Set to indicate file patterns contain regular expressions '
            + '(instead of shell-style glob patterns, the default)')
    parser.add_argument('outfile',
        help='Output file for result (default: stdout)')
    args = parser.parse_args()
    result = main(args.source_dir, args.target_dir, re.escape(args.pattern),
        args.regex, args.outfile)
    sys.exit(result)
