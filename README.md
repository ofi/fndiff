# fndiff

## Purpose

List all files from one directory with according to selection pattern whose
basenames are (not) present in another (or same) directory with another
extension (or same extension if directories differ).


## Usage

From the script's help output:

        usage: fndiff [-h] [-s SOURCE_DIR] [-p PATTERN] [-r] [-o OUTFILE] [target_dir]

        Diff Filenames by Pattern

        positional arguments:
        target_dir            Target directory with files to compare by common
                                pattern to source

        optional arguments:
        -h, --help            show this help message and exit
        -s SOURCE_DIR, --source-dir SOURCE_DIR
                                Source directory serving as reference (default: cwd)
        -p PATTERN, --pattern PATTERN
                                Regular expression to match files from source and
                                target sets optionally containing one or more RE
                                groups to denominate the common part(s) of each
                                matching pair (default is basename, i.e. all
                                characters up to last dot)
        -r, --regex           Set to indicate file patterns contain regular
                                expressions (instead of shell-style glob patterns, the
                                default)
        -o OUTFILE, --outfile OUTFILE
                                Output file for result (default: stdout)


The result will be a list of pathnames of files from the target directory
selected by target pattern, which have no specified counterparts in the source
directory.
A counterpart is defined as a filename with the same ordered groups matched by
the regular expression tranlated from the given shell-style glob pattern on the
source and the target side (see examples to visually get the idea).
Each resulting file is written on a single line.
The path before each file will be printed as given by the taret_dir parameter.

Errors will be printed to stderr as reported by the operating system, e. g. for
missing directories, insufficient access rights etc. An exit code of zero (0)
means success, any other value an error.

An empty result list is not an error!


## Examples

To select all raw Fujifilm image files from dir `RAF` which are missing in
directory `JPG` and print them on stdout:

        fndiff -s JPG -p 'DSCF([0-9]{4})[.][A-Z]{3}$' -r RAF

This interpretes the pattern from `-p` as an regular expression because of `-r`,
looks in the directories `JPG` and `RAF` for all matching files, and reports
all those in the directory `RAF` which do not have a counterpart in the 
directory `JPG`, e.g. a line `DSCF0345.RAF` indicates there is no `DSCF0345.JPG`
in the source directory `JPG`.


## Installation

Assuming Python3 (version >= 3.4 recommmended) is installed on your system, the
steps go:

1. Clone or download the repository.
1. `cd` into the top level directory `fndiff`
1. Install with `pip install .` (using `sudo` where applicable)

## Bugs

Glob style matching only works for full filenames for the time being.

## Motivation

Because loading raw images of my Fujifilm X-pro2 needs a long time,
and because I produce a JPEG image simultaneously in the second
card slot, it's a lot faster to sort and filter pictures by their JPEGs than
RAF-instances.

After having dumped several frames I like to get rid of the costly (in terms
of file space) RAF counterparts as well, but I have not found a tool to 
accomplish this.

Some clever zsh scripting might do it, but nowadays Python is commonly more
available than zsh (or even bash). Instead this package can be used either
manually or by other scripts or programs.

One can argue the solution is "over-engineered", but because the need arose
while preparing a Python workshop, I have decided to craft it in a somewhat
"clean" way as a supplement to the course.


## Legalese

Copyright 2018 Olaf Fiedler, Nürnberg, Germany,
License MIT (see LICENSE file for details)


## Disclaimer

**This software is provided as is without any claim of fitness for any given
purpose. If you use it, you will do so on your solely own risk without any
ability to hold the author(s) responsible for any consequences resulting from
the use of this software.**
