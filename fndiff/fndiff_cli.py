#!/usr/bin/env python3
"""
    fndiff_cli.py -- List unpaired files in directories acc. to name patterns
                    Command Line interface

    See README.md for more information.
    See LICENSE for copyright details.
"""
import argparse
import sys
from .fndiff import fndiff

def main():
    parser = argparse.ArgumentParser(description='Diff Filenames by Pattern')
    parser.add_argument('-s', '--source-dir', default='.',
        help='Source directory with files being compared by name with those '
            + 'from the target directory (default: cwd)')
    parser.add_argument('-p', '--pattern', default=r'(.*)[.].*$',
        help='Regular expression to match files from source and target sets '
            + 'optionally containing one or more RE groups to denominate the '
            + 'common part(s) of each matching pair '
            + '(default is basename, i.e. all characters up to last dot)')
    parser.add_argument('-r', '--regex', action='store_true',
        help='Set to indicate file pattern contains a regular expression '
            + '(instead of shell-style glob patterns, the default)')
    parser.add_argument('-o', '--outfile', default=None,
        help='Output file for result (default: stdout)')
    parser.add_argument('target_dir', nargs='?', default=None,
        help='Target directory with files serving as a reference by name to '
            + 'those in the source directory.')
    args = parser.parse_args()
    (result, msg) = fndiff(args.source_dir, args.target_dir, args.pattern,
        args.regex, args.outfile)
    if result != 0:
        print("{}: {}".format(__name__, msg), file=sys.stderr)
        parser.print_usage(file=sys.stderr)
    sys.exit(result)
