#!/usr/bin/env python3
"""
    fndiff-shfront.py -- List unpaired files in directories acc. to basenames

    See LICENSE for copyright details.
"""

import sys
import re
import FilenamesDiffer


def main(sdir, tdir, pat, rexflag, ofile):
    result = 0
    try:
        differ = FilenamesDiffer.FilenamesDiffer(srcdir=sdir,
            dstdir=tdir, pattern=pat, reflag=rexflag)
        fnlist = differ.not_in_target()
        if ofile is None:
            for item in fnlist:
                print(item)
        else:
            with open(ofile, 'w') as f:
                f.writelines([ str(item) + '\n' for item in fnlist ]) 
    except FilenamesDiffer.FilenamesDiffError as err:
        print(err, file=sys.stderr)
        result = 1
    return result


if __name__ == '__main__':
    import argparse
    import sys

    parser = argparse.ArgumentParser(description='Diff Filenames by Pattern')
    parser.add_argument('-s', '--source-dir', default='.',
        help='Source directory serving as reference (default: cwd)')
    parser.add_argument('-p', '--pattern', default=r'(.*)[.].*$',
        help='Regular expression to match files from source and target sets '
            + 'optionally containing one or more RE groups to denominate the '
            + 'common part(s) of each matching pair '
            + '(default is basename, i.e. all characters up to last dot)')
    parser.add_argument('-r', '--regex', action='store_true',
        help='Set to indicate file patterns contain regular expressions '
            + '(instead of shell-style glob patterns, the default)')
    parser.add_argument('-o', '--outfile', default=None,
        help='Output file for result (default: stdout)')
    parser.add_argument('target_dir', nargs='?',
        help='Target directory with files to compare by common pattern to source')
    args = parser.parse_args()
    result = main(args.source_dir, args.target_dir, args.pattern,
        args.regex, args.outfile)
    sys.exit(result)
