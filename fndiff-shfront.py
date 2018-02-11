#!/usr/bin/env python3
"""
    fndiff-shfront.py -- List unpaired files in directories acc. to basenames

    See LICENSE for copyright details.
"""

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

def main(sdir, spat, tdir, tpat, rexflag, ofile):
    result = 0
    try:
        differ = FilenamesDiffer.FilenamesDiffer(srcdir=sdir, srcpattern=spat,
            dstdir=tdir, dstpat=tpat, reflag=rexflag)
        fnlist = differ.diff_it()
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
        help='Pattern of files to consider (default: all)')
    parser.add_argument('-T', '--target-dir', required=True,
        help='Target directory with files to compare by name to source')
    parser.add_argument('-t', '--target-suffix', default='*',
        help='Extensions (after last dot) of files to include in comparison '
            + 'by corresponding basename or none for full filename compare.')
    parser.add_argument('-r', '--regex', action='store_true',
        help='Set to indicate patterns contiain regular expressions '
            + '(instead of shell-style glob patterns, the default)')
    parser.add_argument('outfile',
        help='Output file for result (default: stdout)')
    args = parser.parse_args()
    result = main(args.source_dir, args.source_pattern, args.target_dir,
        args.target_suffix, args.regex, args.outfile)
    sys.exit(result)
